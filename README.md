**Genetic Algorithm for String Optimization in Python**

A Python based implementation of a genetic algorithm, 'GeneticGuess Sentencer', designed to solve a string-matching optimization problem from first principles.

**The Challenge**

The goal of this project was to implement a complete genetic algorithm to evolve a random population of strings towards a user defined target sentence.

A key constraint was the prohibition of Python's advanced data structures (e.g., lists, sets, classes), requiring an implementation based purely on fundamental string manipulation, loops, and conditional logic. This constraint necessitated a deep, practical understanding of the algorithm's core components and their implementation from scratch.

**Key Features & Skills Demonstrated**

-> **Algorithm Architecture:** Architected a complete genetic algorithm in Python, applying principles of evolutionary computation to solve a complex optimization problem.

-> **First-Principles Implementation:** Implemented the entire algorithm from scratch without relying on advanced libraries or data structures, showcasing a strong grasp of core computer science fundamentals.

-> **Genetic Operator Engineering:**

  --> **Tournament Selection:** Engineered a custom tournament selection operator to effectively identify high-performing individuals for reproduction.

  --> **Single-Point Crossover:** Implemented a crossover operator to combine genetic material from parent strings, driving generational improvement.

  --> **Mutation:** Developed a mutation operator to introduce diversity into the population, preventing premature convergence on local optima.

-> **Fitness Function Tuning:** Designed and fine-tuned the core fitness function to accurately measure a solution's proximity to the target, directly guiding the evolutionary selection process.

-> **Hyperparameter Calibration:** Calibrated operator probabilities (mutation and crossover) to effectively balance solution space exploration and exploitation, ensuring consistent and rapid convergence.
