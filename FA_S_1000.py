import numpy as np
import time
import pandas as pd

def styblinski_tang(x):
    """Styblinski-Tang function."""
    return sum((xi**4 - 16 * xi**2 + 5 * xi) / 2 for xi in x)

def update(Xi, Xj, scale, alpha, beta0, gamma):
    r = np.linalg.norm(Xi - Xj)
    beta = beta0 * np.exp(-gamma * r**2)
    steps = alpha * (np.random.rand() - 0.5) * scale
    return Xi + beta * (Xj - Xi) + steps

def checkbounds(X, Lb, Ub):
    return np.clip(X, Lb, Ub)

def firefly_styblinski_tang(D=2, N=5, iter_max=30, alpha=1.0, beta0=1.0, gamma=0.01, theta=0.97):
    lb = -5
    ub = 5
    Lb = lb * np.ones(D)  # Lower bounds for Styblinski-Tang function
    Ub = ub * np.ones(D)  # Upper bounds for Styblinski-Tang function
    scale = np.abs(Ub - Lb)

    pop = np.random.uniform(Lb, Ub, (N, D))
    fx = np.array([styblinski_tang(individual) for individual in pop])

    for iter in range(iter_max):
        for i in range(N):  # for all the fireflies
            for j in range(N):  # for all the fireflies
                if fx[j] < fx[i]:  # if j is more attractive than i
                    Xnew = update(pop[i], pop[j], scale, alpha, beta0, gamma)
                    Xnew = checkbounds(Xnew, Lb, Ub)
                    fnew = styblinski_tang(Xnew)
                    if fnew < fx[i]:  # if fnew is better than fx[i]
                        pop[i] = Xnew
                        fx[i] = fnew

        alpha *= theta  # Reduce alpha by factor theta

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
iter_max = 1000
runs = 31

results = []

# Run the FA algorithm for different dimensions and populations
for D in dimensions:
    for N in populations[D]:
        start_time = time.time()
        values = [firefly_styblinski_tang(D, N, iter_max)[0] for _ in range(runs)]
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
    filename = f"FA_S_1000 {D}.csv"
    df.to_csv(filename, index=False)
    results = []
