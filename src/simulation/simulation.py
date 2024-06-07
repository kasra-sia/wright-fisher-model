from src.simulation.population import Population

def run_wright_fisher_simulation(nInd, p0, nGen, nRuns):
    populations = [Population(nInd, p0) for _ in range(nRuns)]
    for pop in populations:
        pop.evolve(nGen)
    return populations
