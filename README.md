# Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions

# Assignment 1

## I. Introduction

Swarm-based algorithms, exemplified by Particle Swarm Optimization (PSO), Artificial Bee Colony (ABC), and Firefly Algorithm (FA), represent a significant advancement in solving complex optimization problems that challenge conventional algorithms. These algorithms draw inspiration from the natural behaviors of swarms, such as birds flocking or bees foraging, to navigate through multi-dimensional search spaces to find optimal solutions. The complexity and non-linearity of certain functions often require sophisticated methods like these to efficiently locate the global minimum.

PSO, ABC, and FA have gained popularity across various fields due to their flexibility and effectiveness in handling non-linear and multi-modal optimization challenges. Each algorithm has unique characteristics and mechanisms: 

- **PSO** mimics the social behavior of birds.
- **ABC** simulates the foraging behavior of honeybees.
- **FA** is inspired by the bioluminescent communication of fireflies.

This study uses two benchmark functions, Rastrigin and Styblinski-Tang, to compare these three swarm-based algorithms with different algorithm configurations.

## II. Test Functions

### 1. Rastrigin Function
- **Definition:**
  \( f(x) = 10n + \sum_{i=1}^{n}[x_i^2 + 10 \cos(2\pi x_i)] \)
- **Search domain:** \(-5.12 \leq x_i \leq 5.12\)
- **Global minimum:** \(x^* = (0, 0, ..., 0), f(x^*) = 0\)

### 2. Styblinski-Tang Function
- **Definition:**
  \( f(x) = \frac{1}{2} \sum_{i=1}^{n}(x_i^4 - 16x_i^2 + 5x_i) \)
- **Search domain:** \(-5 \leq x_i \leq 5\)
- **Global minimum:** \(x^* = (2.903534, 2.903534, ..., 2.903534), f(x^*) = -39.16599n\)

## III. Metaheuristic Algorithms

### 1. Particle Swarm Optimization (PSO)
PSO is an optimization technique guided by the group dynamics observed in birds and fish. Each particle adjusts its speed according to its own best discovery and the top discovery of the entire group, aiding in the search for the optimum result.

### 2. Artificial Bee Colony Algorithm (ABC)
The ABC algorithm mimics the way honeybees forage for food. A group of bees scours the search area to pinpoint the best solution. Every bee remembers the top solution it discovers and communicates this data with the rest of the group.

### 3. Firefly Algorithm (FA)
FA is an optimization algorithm inspired by the glow patterns of fireflies. Each firefly is drawn to others that shine more brightly, moving towards them based on their glow intensity.

## IV. Computational Experiment

### 1. Design of Experiment
- **Benchmark functions:** Rastrigin, Styblinski-Tang
- **Dimensions (D):** \(2, 4, 10, 50\)
- **Population (N):** \(1\times, 3\times, 5\times, 7\times\) dimension size
- **Max iterations:** 50, 1000
- **Number of runs per function:** 31
- **Search range:** \([-5.12, 5.12] \text{ for Rastrigin, } [-5, 5] \text{ for Styblinski-Tang}\)

### 2. Experimental Results
#### Rastrigin Function
- **PSO:**
  - Lower dimensions exhibit good convergence.
  - High dimensions pose challenges despite increased population sizes.
### Max iteration = 50
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_R_50/PSO_R_50_2.png" alt="PSO_R_50_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_R_50/PSO_R_50_4.png" alt="PSO_R_50_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_R_50/PSO_R_50_10.png" alt="PSO_R_50_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_R_50/PSO_R_50_50.png" alt="PSO_R_50_50" width="30%">
</div>

### Max iteration = 1000
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_R_1000/PSO_R_1000_2.png" alt="PSO_R_1000_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_R_1000/PSO_R_1000_4.png" alt="PSO_R_1000_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_R_1000/PSO_R_1000_10.png" alt="PSO_R_1000_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_R_1000/PSO_R_1000_50.png" alt="PSO_R_1000_50" width="30%">
</div>

- **ABC:**
  - Improved performance with larger populations.
  - High dimensions see diminishing returns.
### Max iteration = 50
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_R_50/ABC_R_50_2.png" alt="ABC_R_50_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_R_50/ABC_R_50_4.png" alt="ABC_R_50_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_R_50/ABC_R_50_10.png" alt="ABC_R_50_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_R_50/ABC_R_50_50.png" alt="ABC_R_50_50" width="30%">
</div>

### Max iteration = 1000
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_R_1000/ABC_R_1000_2.png" alt="PSO_R_1000_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_R_1000/ABC_R_1000_4.png" alt="PSO_R_1000_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_R_1000/ABC_R_1000_10.png" alt="PSO_R_1000_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_R_1000/ABC_R_1000_50.png" alt="PSO_R_1000_50" width="30%">
</div>

- **FA:**
  - Higher iterations significantly enhance solution quality.
  - Increased runtime with larger populations and dimensions.
### Max iteration = 50
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_R_50/FA_R_50_2.png" alt="FA_R_50_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_R_50/FA_R_50_4.png" alt="FA_R_50_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_R_50/FA_R_50_10.png" alt="FA_R_50_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_R_50/FA_R_50_50.png" alt="FA_R_50_50" width="30%">
</div>

### Max iteration = 1000
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_R_1000/FA_R_1000_2.png" alt="FA_R_1000_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_R_1000/FA_R_1000_4.png" alt="FA_R_1000_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_R_1000/FA_R_1000_10.png" alt="FA_R_1000_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_R_1000/FA_R_1000_50.png" alt="FA_R_1000_50" width="30%">
</div>

#### Styblinski-Tang Function
- **PSO:**
  - Consistently achieves closer approximations to the global minimum.
  - Clear trade-off between computational effort and solution quality.
### Max iteration = 50
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_S_50/PSO_S_50_2.png" alt="PSO_S_50_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_S_50/PSO_S_50_4.png" alt="PSO_S_50_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_S_50/PSO_S_50_10.png" alt="PSO_S_50_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_S_50/PSO_S_50_50.png" alt="PSO_S_50_50" width="30%">
</div>

### Max iteration = 1000
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_S_1000/PSO_S_1000_2.png" alt="PSO_S_1000_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_S_1000/PSO_S_1000_4.png" alt="PSO_S_1000_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_S_1000/PSO_S_1000_10.png" alt="PSO_S_1000_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/PSO/PSO_S_1000/PSO_S_1000_50.png" alt="PSO_S_1000_50" width="30%">
</div>

- **ABC:**
  - Better convergence with larger populations.
  - Increased runtime in higher dimensions.

### Max iteration = 50
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_S_50/ABC_S_50_2.png" alt="ABC_S_50_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_S_50/ABC_S_50_4.png" alt="ABC_S_50_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_S_50/ABC_S_50_10.png" alt="ABC_S_50_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_S_50/ABC_S_50_50.png" alt="ABC_S_50_50" width="30%">
</div>

### Max iteration = 1000
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_S_1000/ABC_S_1000_2.png" alt="PSO_S_1000_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_S_1000/ABC_S_1000_4.png" alt="PSO_S_1000_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_S_1000/ABC_S_1000_10.png" alt="PSO_S_1000_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/ABC/ABC_S_1000/ABC_S_1000_50.png" alt="PSO_S_1000_50" width="30%">
</div>

- **FA:**
  - Improved optimization outcomes with higher iterations.
  - Trade-off between computational efficiency and accuracy.
### Max iteration = 50
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_S_50/FA_S_50_2.png" alt="FA_S_50_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_S_50/FA_S_50_4.png" alt="FA_S_50_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_S_50/FA_S_50_10.png" alt="FA_S_50_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_S_50/FA_S_50_50.png" alt="FA_S_50_50" width="30%">
</div>

### Max iteration = 1000
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_S_1000/FA_S_1000_2.png" alt="FA_S_1000_2" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_S_1000/FA_S_1000_4.png" alt="FA_S_1000_4" width="30%">
</div>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_S_1000/FA_S_1000_10.png" alt="FA_S_1000_10" width="30%">
  <img src="https://github.com/OwentsaiTTS/Performance-Comparison-of-Swarm-Based-Algorithms-on-Benchmark-Functions/blob/main/Plot/FA/FA_S_1000/FA_S_1000_50.png" alt="FA_S_1000_50" width="30%">
</div>

## V. Conclusion

In summary, the comparative analysis of PSO, ABC, and FA reveals:
- **PSO**: Fastest and most consistent overall.
- **ABC**: Excels in solving discrete problems.
- **FA**: Effective in navigating complex multimodal landscapes.

Each algorithm demonstrates unique strengths depending on the problem scenario, making them valuable tools in optimization research.
