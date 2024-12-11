import numpy as np
import time
import pandas as pd

def rastrigin(x):
    """Rastrigin function."""
    return 10 * len(x) + sum(xi**2 - 10 * np.cos(2 * np.pi * xi) for xi in x)

def update(Xi, Xj, scale, alpha, beta0, gamma):
    r = np.linalg.norm(Xi - Xj)
    beta = beta0 * np.exp(-gamma * r**2)
    steps = alpha * (np.random.rand() - 0.5) * scale
    return Xi + beta * (Xj - Xi) + steps

def checkbounds(X, Lb, Ub):
    return np.clip(X, Lb, Ub)

def firefly_rastrigin(D, N, iter_max=30, alpha=1.0, beta0=1.0, gamma=0.01, theta=0.97):
    lb = -5.12
    ub = 5.12
    Lb = lb * np.ones(D)
    Ub = ub * np.ones(D)
    scale = np.abs(Ub - Lb)

    pop = np.random.uniform(Lb, Ub, (N, D))
    fx = np.array([rastrigin(individual) for individual in pop])

    for iter in range(iter_max):
        for i in range(N):
            for j in range(N):
                if fx[j] < fx[i]:
                    Xnew = update(pop[i], pop[j], scale, alpha, beta0, gamma)
                    Xnew = checkbounds(Xnew, Lb, Ub)
                    fnew = rastrigin(Xnew)
                    if fnew < fx[i]:
                        pop[i] = Xnew
                        fx[i] = fnew

        alpha *= theta

    optval = np.min(fx)
    optindx = np.argmin(fx)
    return optval, pop[optindx]

# Setup for different dimensions and populations
dimensions = [2, 4, 10, 50]
populations = {
    2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    4: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28],
    10: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    50: [25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350]
}
iter_max = 50
runs = 31

results = []

# Run the FA algorithm for different dimensions and populations
for D in dimensions:
    for N in populations[D]:
        start_time = time.time()
        values = [firefly_rastrigin(D, N, iter_max)[0] for _ in range(runs)]
        end_time = time.time()

        mean_value = round(np.mean(values), 4)
        min_value = round(min(values), 4)
        variance = round(np.var(values), 4)
        std_deviation = round(np.std(values), 4)
        runtime = round((end_time - start_time) / runs, 4)  # milliseconds

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
    filename = f"FA_R_50 {D}.csv"
    df.to_csv(filename, index=False)
    results = []