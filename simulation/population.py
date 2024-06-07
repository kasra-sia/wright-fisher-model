import numpy as np

class Population:
    def __init__(self, nInd, p0):
        self.nInd = nInd
        self.p0 = p0
        self.initial_population = np.zeros(self.nInd)
        self.initial_population[0:int(p0 * self.nInd)] = 1
        np.random.shuffle(self.initial_population)
        self.history = [self.initial_population]

    def generation(self):
        return np.random.choice(self.history[-1], self.nInd, replace=True)

    def evolve(self, nGen):
        for _ in range(nGen):
            self.history.append(self.generation())
        self.get_trajectory()

    def get_trajectory(self):
        self.traj = np.mean(self.history, axis=1)
        return self.traj

    def plot_trajectory(self):
        import matplotlib.pyplot as plt
        plt.plot(self.traj)
        plt.xlabel("Generation")
        plt.ylabel("Allele Frequency")
        plt.show()
