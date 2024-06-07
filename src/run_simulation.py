from simulation.simulation import run_wright_fisher_simulation
from simulation.plotting import plot_trajectories
from simulation.analysis import fixation_probability
# Parameters
nInd = 137
p0 = 0.3
nGen = 100
nRuns = 100

# Run the simulation
populations = run_wright_fisher_simulation(nInd, p0, nGen, nRuns)
fix_prob = fixation_probability(populations)
print(f"Fixation probability: {fix_prob}")

# Plot the results
plot_trajectories(populations)
# plctories()