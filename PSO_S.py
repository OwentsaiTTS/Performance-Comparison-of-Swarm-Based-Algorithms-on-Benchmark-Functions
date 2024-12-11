import numpy as np
import time
import pandas as pd  # Import pandas for handling data

def styblinski_tang(x):
    """Styblinski-Tang function."""
    return sum((xi**4 - 16 * xi**2 + 5 * xi) / 2 for xi in x)

def pso_styblinski_tang(D=2, N=5, iter_max=30):
    """Particle Swarm Optimization for Styblinski-Tang function."""
    # Initialize parameters
    Lb = -5 * np.ones(D)  # Lower bounds for Styblinski-Tang function
    Ub = 5 * np.ones(D)  # Upper bounds for Styblinski-Tang function
    wmax = 0.9  # Inertia weight max
    wmin = 0.1  # Inertia weight min
    c1max = 2.05  # Personal learning coefficient max
    c1min = 0    # Personal learning coefficient min
    c2max = 2.05  # Global learning coefficient max
    c2min = 0    # Global learning coefficient min

    # Initialize the particle's position and velocity
    pos = np.random.uniform(Lb, Ub, (N, D))
    vel = np.random.uniform(-1, 1, (N, D))

    # Initialize personal best position and value
    pbest = pos.copy()
    pbestval = np.array([styblinski_tang(p) for p in pbest])

    # Initialize global best position and value
    gbest = pbest[pbestval.argmin()]
    gbestval = pbestval.min()

    # PSO algorithm main loop
    for it in range(iter_max):
        w = wmax - (wmax - wmin) * it / iter_max  # Linearly decreasing w
        c1 = c1max - (c1max - c1min) * it / iter_max  # Dynamically adjusting c1
        c2 = c2max - (c2max - c2min) * it / iter_max  # Dynamically adjusting c2

        # Update position and velocity of each particle
        for i in range(N):
            r1, r2 = np.random.rand(2)  # Random numbers for stochastic components
            vel[i] = w * vel[i] + c1 * r1 * (pbest[i] - pos[i]) + c2 * r2 * (gbest - pos[i])
            pos[i] = pos[i] + vel[i]

            # Apply boundary conditions
            pos[i] = np.clip(pos[i], Lb, Ub)

            # Update personal best
            if styblinski_tang(pos[i]) < pbestval[i]:
                pbest[i] = pos[i]
                pbestval[i] = styblinski_tang(pos[i])

        # Update global best
        if min(pbestval) < gbestval:
            gbest = pbest[pbestval.argmin()]
            gbestval = pbestval.min()

    return gbest, gbestval

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

# Run the PSO algorithm for different dimensions and populations
for D in dimensions:
    for N in populations[D]:
        start_time = time.time()
        values = [pso_styblinski_tang(D, N, iter_max)[1] for _ in range(runs)]
        end_time = time.time()

        mean_value = round(np.mean(values), 4)
        min_value = round(min(values), 4)
        variance = round(np.var(values), 4)
        std_deviation = round(np.std(values), 4)
        runtime = round((end_time - start_time) / runs, 4)  # Average runtime per run in milliseconds

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
    filename = f"PSO_S_1000 {D}.csv"
    df.to_csv(filename, index=False)
    results = []