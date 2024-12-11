import numpy as np
import time
import pandas as pd

def rastrigin(x):
    """Rastrigin function."""
    return 10 * len(x) + sum(xi**2 - 10 * np.cos(2 * np.pi * xi) for xi in x)

def abc_rastrigin(D, N, iter_max):
    """Artificial Bee Colony (ABC) algorithm for Rastrigin function."""
    lb = -5.12
    ub = 5.12
    Lb = lb * np.ones(D)
    Ub = ub * np.ones(D)
    limit = D
    trial = np.zeros(N)
    pos = np.zeros((N, D))
    fx = np.ones(N) * np.inf

    for i in range(N):
        pos[i] = Lb + (Ub - Lb) * np.random.rand(D)
        fx[i] = rastrigin(pos[i])

    for it in range(iter_max):
        for i in range(N):
            Xnew = np.copy(pos[i])
            d = np.random.randint(D)
            partner = np.random.randint(N)
            while partner == i:
                partner = np.random.randint(N)

            X = pos[i, d]
            Xp = pos[partner, d]
            Xnew[d] = X + (np.random.rand() - 0.5) * 2 * (X - Xp)
            Xnew = np.clip(Xnew, Lb, Ub)

            fnew = rastrigin(Xnew)
            if fnew < fx[i]:
                pos[i] = Xnew
                fx[i] = fnew
                trial[i] = 0
            else:
                trial[i] += 1

        prob = fx / np.sum(fx)

        for i in range(N):
            if np.random.rand() < prob[i]:
                Xnew = np.copy(pos[i])
                d = np.random.randint(D)
                partner = np.random.randint(N)
                while partner == i:
                    partner = np.random.randint(N)

                X = pos[i, d]
                Xp = pos[partner, d]
                Xnew[d] = X + (np.random.rand() - 0.5) * 2 * (X - Xp)
                Xnew = np.clip(Xnew, Lb, Ub)

                fnew = rastrigin(Xnew)
                if fnew < fx[i]:
                    pos[i] = Xnew
                    fx[i] = fnew
                    trial[i] = 0
                else:
                    trial[i] += 1

        for i in range(N):
            if trial[i] > limit:
                pos[i] = Lb + (Ub - Lb) * np.random.rand(D)
                fx[i] = rastrigin(pos[i])
                trial[i] = 0

    best_index = np.argmin(fx)
    best_solution = pos[best_index]
    best_fitness = fx[best_index]

    return best_solution, best_fitness

# Setup for different dimensions and populations
dimensions = [2, 4, 10, 50]
populations = {
    2: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    4: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28],
    10: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    50: [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350]
}
iter_max = 1000
runs = 31

results = []

# Run the ABC algorithm for different dimensions and populations
for D in dimensions:
    for N in populations[D]:
        start_time = time.time()
        values = [abc_rastrigin(D, N, iter_max)[1] for _ in range(runs)]
        end_time = time.time()

        mean_value = round(np.mean(values), 4)
        min_value = round(min(values), 4)
        variance = round(np.var(values), 4)
        std_deviation = round(np.std(values), 4)
        runtime = round((end_time - start_time) / runs, 4)

        results.append({
            'Dimension': D,
            'Population': N,
            'Mean Value': mean_value,
            'Best Value': min_value,
            'Variance': variance,
            'Std. Deviation': std_deviation,
            'Runtime(s)': runtime
        })

    # Convert results to a pandas DataFrame
    df = pd.DataFrame(results)

    # Save the DataFrame to an csv file
    filename = f"ABC_R_1000 {D}.csv"
    df.to_csv(filename, index=False)
    results = []
