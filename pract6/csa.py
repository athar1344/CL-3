import numpy as np
import random

# -------------------------------
# Problem: Minimize Sphere Function
def objective_function(x):
    return np.sum(x**2)

# -------------------------------
# Parameters
POP_SIZE = 20
DIM = 5
GENERATIONS = 50
CLONE_FACTOR = 5
MUTATION_RATE = 0.1
LOWER_BOUND = -5
UPPER_BOUND = 5

# -------------------------------
# Initialize population
def initialize_population():
    return [np.random.uniform(LOWER_BOUND, UPPER_BOUND, DIM) for _ in range(POP_SIZE)]

# -------------------------------
# Affinity (lower is better)
def calculate_affinity(population):
    return [(antibody, objective_function(antibody)) for antibody in population]

# -------------------------------
# Selection (top antibodies)
def select_best(pop_affinity):
    pop_affinity.sort(key=lambda x: x[1])  # minimize
    return pop_affinity[:POP_SIZE // 2]

# -------------------------------
# Cloning
def clone(selected):
    clones = []
    for antibody, affinity in selected:
        num_clones = int(CLONE_FACTOR / (affinity + 1e-6))  # more clones for better
        for _ in range(num_clones):
            clones.append(np.copy(antibody))
    return clones

# -------------------------------
# Mutation
def mutate(clones):
    mutated = []
    for clone in clones:
        if random.random() < MUTATION_RATE:
            noise = np.random.normal(0, 0.5, DIM)
            clone = clone + noise
            clone = np.clip(clone, LOWER_BOUND, UPPER_BOUND)
        mutated.append(clone)
    return mutated

# -------------------------------
# Main CSA Algorithm
population = initialize_population()

for gen in range(GENERATIONS):
    # Evaluate affinity
    pop_affinity = calculate_affinity(population)

    # Select best
    selected = select_best(pop_affinity)

    # Clone
    clones = clone(selected)

    # Mutate
    mutated_clones = mutate(clones)

    # New population (elitism + mutated clones)
    new_population = [antibody for antibody, _ in selected]
    new_population.extend(mutated_clones)

    # Keep population size fixed
    population = new_population[:POP_SIZE]

    # Best solution
    best = min(population, key=objective_function)
    print(f"Generation {gen} Best Fitness: {objective_function(best):.6f}")

# -------------------------------
# Final result
best_solution = min(population, key=objective_function)

print("\nBest Solution Found:", best_solution)
print("Best Fitness:", objective_function(best_solution))