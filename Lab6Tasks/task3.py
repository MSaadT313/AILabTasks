import random

# Problem Definition
MAX_WEIGHT = 30

# Items: (weight, survival points)
items = [
    (5, 10),
    (8, 15),
    (3, 7),
    (7, 12),
    (4, 8),
    (6, 11),
    (2, 5),
    (9, 18)
]

NUM_ITEMS = len(items)

# GA Parameters
POP_SIZE = 6
GENERATIONS = 50
MUTATION_RATE = 0.1


# Generate random chromosome (0/1 for each item)
def generate_chromosome():
    return [random.randint(0, 1) for _ in range(NUM_ITEMS)]


# Fitness function
def fitness(chromosome):
    total_weight = 0
    total_value = 0

    for i in range(NUM_ITEMS):
        if chromosome[i] == 1:
            total_weight += items[i][0]
            total_value += items[i][1]

    # Penalize overweight solutions
    if total_weight > MAX_WEIGHT:
        return 0

    return total_value


# Selection (Tournament Selection)
def select(population):
    a = random.choice(population)
    b = random.choice(population)
    return a if fitness(a) > fitness(b) else b


# Crossover (Single Point)
def crossover(parent1, parent2):
    point = random.randint(1, NUM_ITEMS - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


# Mutation
def mutate(chromosome):
    for i in range(NUM_ITEMS):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]  # flip bit
    return chromosome


# Genetic Algorithm
def genetic_algorithm():
    # Initial population
    population = [generate_chromosome() for _ in range(POP_SIZE)]

    for _ in range(GENERATIONS):
        new_population = []

        while len(new_population) < POP_SIZE:
            # Selection
            parent1 = select(population)
            parent2 = select(population)

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            child1 = mutate(child1)
            child2 = mutate(child2)

            new_population.extend([child1, child2])

        population = new_population[:POP_SIZE]

    # Get best solution
    best = max(population, key=fitness)
    return best, fitness(best)


# ---- Execution ----
if __name__ == "__main__":
    best_solution, best_value = genetic_algorithm()

    print("Best Selection (1=Selected, 0=Not Selected):")
    print(best_solution)

    total_weight = sum(items[i][0] for i in range(NUM_ITEMS) if best_solution[i] == 1)

    print("Total Survival Points:", best_value)
    print("Total Weight:", total_weight)