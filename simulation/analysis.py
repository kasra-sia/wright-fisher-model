import numpy as np

def frequency_at_generation(populations, generation):
    return np.array([pop.traj[generation] for pop in populations])

def calculate_variance(populations, generation):
    freqs = frequency_at_generation(populations, generation)
    return np.var(freqs)

def fixation_probability(populations):
    """
    Calculate the proportion of populations that have fixed the allele.
    """
    fixed_count = sum([pop.traj[-1] == 1 or pop.traj[-1] == 0 for pop in populations])
    return fixed_count / len(populations)

def time_to_fixation(populations):
    """
    Calculate the time to fixation for each population.
    Return the list of fixation times.
    """
    fixation_times = []
    for pop in populations:
        traj = pop.traj
        fixed = np.where((traj == 0) | (traj == 1))[0]
        if len(fixed) > 0:
            fixation_times.append(fixed[0])
    return fixation_times
