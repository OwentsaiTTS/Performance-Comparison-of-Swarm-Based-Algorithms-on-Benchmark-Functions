import numpy as np
import time
import pandas as pd

def styblinski_tang(x):
    """Styblinski-Tang function."""
    return sum((xi**4 - 16 * xi**2 + 5 * xi) / 2 for xi in x)

def abc_styblinski_tang(D, food_sources, iter_max):
    lb = -5
    ub = 5
    Lb = lb * np.ones(D)
    Ub = ub * np.ones(D)

    food_positions = np.random.uniform(Lb, Ub, (food_sources, D))
    food_fitness = np.array([styblinski_tang(position) for position in food_positions])
    trial_counters = np.zeros(food_sources)

    for it in range(iter_max):
        for i in range(food_sources):
            phi = np.random.uniform(-1, 1, D)
            k = np.random.randint(0, food_sources)
            while k == i:
                k = np.random.randint(0, food_sources)

            new_solution = food_positions[i] + phi * (food_positions[i] - food_positions[k])
            new_solution = np.clip(new_solution, Lb, Ub)
            new_fitness = styblinski_tang(new_solution)

            if new_fitness < food_fitness[i]:
                food_positions[i] = new_solution
                food_fitness[i] = new_fitness
                trial_counters[i] = 0
            else:
                trial_counters[i] += 1

        # 计算每个食物源的适应度概率
        fitness_prob = 1.0 / (1.0 + np.abs(food_fitness))
        fitness_prob /= fitness_prob.sum()

        for _ in range(food_sources):
            i = np.random.choice(food_sources, p=fitness_prob)
            phi = np.random.uniform(-1, 1, D)
            k = np.random.randint(0, food_sources)
            while k == i:
                k = np.random.randint(0, food_sources)

            new_solution = food_positions[i] + phi * (food_positions[i] - food_positions[k])
            new_solution = np.clip(new_solution, Lb, Ub)
            new_fitness = styblinski_tang(new_solution)

            if new_fitness < food_fitness[i]:
                food_positions[i] = new_solution
                food_fitness[i] = new_fitness
                trial_counters[i] = 0
            else:
                trial_counters[i] += 1

        for i in range(food_sources):
            if trial_counters[i] > D:
                food_positions[i] = np.random.uniform(Lb, Ub, D)
                food_fitness[i] = styblinski_tang(food_positions[i])
                trial_counters[i] = 0

    best_index = np.argmin(food_fitness)
    best_solution = food_positions[best_index]
    best_fitness = food_fitness[best_index]

    return best_solution, best_fitness

# Setup for different dimensions and food sources
dimensions = [2, 4, 10, 50]
food_sources_list = {
    2: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    4: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28],
    10: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    50: [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350]
}
iter_max = 1000
runs = 31

results = []

for D in dimensions:
    for food_sources in food_sources_list[D]:
        start_time = time.time()
        values = [abc_styblinski_tang(D, food_sources, iter_max)[1] for _ in range(runs)]
        end_time = time.time()

        mean_value = round(np.mean(values), 4)
        min_value = round(min(values), 4)
        variance = round(np.var(values), 4)
        std_deviation = round(np.std(values), 4)
        runtime = round((end_time - start_time) / runs, 4)

        results.append({
            'Dimension': D,
            'Food Sources': food_sources,
            'Mean Value': mean_value,
            'Best Value': min_value,
            'Variance': variance,
            'Std. Deviation': std_deviation,
            'Runtime(s)': runtime
        })

    # Convert results to a pandas DataFrame
    df = pd.DataFrame(results)

    # Save the DataFrame to an csv file
    filename = f"ABC_S_1000 {D}.csv"
    df.to_csv(filename, index=False)
    results = []    
