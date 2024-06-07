import matplotlib.pyplot as plt

def plot_trajectories(populations):
    for pop in populations:
        plt.plot(pop.traj)
    plt.xlabel("Generation")
    plt.ylabel("Allele Frequency")
    plt.show()

def plot_frequency_distribution(populations, generation, nBins=11):
    frequencies = [pop.traj[generation] for pop in populations]
    plt.hist(frequencies, bins=nBins, range=(0, 1))
    plt.xlabel("Allele Frequency")
    plt.ylabel("Number of Populations")
    plt.show()

def plot_fixation_times(fixation_times):
    plt.hist(fixation_times, bins=20, range=(0, max(fixation_times)))
    plt.xlabel("Generations")
    plt.ylabel("Number of Populations")
    plt.title("Distribution of Fixation Times")
    plt.show()
