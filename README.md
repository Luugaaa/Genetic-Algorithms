# Genetic Algorithms Exploration

This repository explores the application of genetic algorithms to solve game theory problems. The focus is on using these algorithms to optimize strategies in two-player games. The projects within this repository stem from academic exercises but have been reimagined to explore more advanced topics in algorithmic optimization.

## Project 1: Strategic Optimization in Pair-Impair Game

### Problem Description

We consider a two-player game with the following rules:
- Both players simultaneously declare "even" or "odd."
- If both players declare the same (either both "even" or both "odd"), Player 1 wins 1 euro, and Player 2 loses 1 euro.
- If one declares "even" and the other "odd," Player 2 wins 1 euro, and Player 1 loses 1 euro.

The goal is to determine the optimal strategy for each player, defined by probabilities of choosing "even" or "odd" that maximize their expected gains.

### Genetic Algorithm Approach

1. **Population Initialization**: We create two populations, each representing a set of strategies for Player 1 and Player 2, respectively. Each strategy in the population is randomly initialized with different probabilities of choosing "even" or "odd."

2. **Fitness Evaluation**: The fitness of a strategy is determined by its expected gain when pitted against the opposing population. For each strategy in Population 1, we evaluate its performance against all strategies in Population 2, and vice versa.

3. **Selection and Mutation**:
   - Identify the best and worst-performing strategies in each population.
   - Replace the worst strategy with a mutated version of the best strategy to ensure exploration of new strategies.
   - Repeat this process for a set number of iterations to evolve optimal strategies.

#### Convergence Analysis

- **Population Size Impact**: With larger populations (e.g., \( N1 = N2 = 100 \)), the algorithm quickly converges to a stable set of strategies where both players have an approximately equal chance of winning. The convergence rate is slower with smaller populations, where strategies tend to oscillate more before stabilizing.

- **Optimal Strategies**: After sufficient iterations (e.g., \( \text{iterations} = 1000 \)), the optimal strategy for Player 1 is to play "even" with a probability of 0.5 and "odd" with a probability of 0.5. The same holds true for Player 2, indicating that in this zero-sum game, the best strategy is a mixed one with equal probabilities.

- **Rock-Paper-Scissors Extension**: When applying the genetic algorithm to the Rock-Paper-Scissors game, the optimal strategy evolved to an equal probability of 1/3 for each move, confirming the Nash equilibrium for this game.


## Project 2: Optimal Strategies in Poker-Like Game

### Problem Description

This game involves two players who independently draw a number between 0 and 1 from a uniform distribution. Player 1 decides whether to bet or not, while Player 2 decides whether to call or fold based on their drawn number.

The possible outcomes are as follows:
- If Player 1 bets and Player 2 folds, Player 1 wins 1 euro, and Player 2 loses 1 euro.
- If Player 1 bets and Player 2 calls:
  - Player 1 wins 1+B euros (B is the bet amount) if Player 1's number is greater.
  - Player 2 wins 1+B euros if Player 2's number is greater.
  - The game is a tie if the numbers are equal, and no one wins or loses.
- If Player 1 does not bet, Player 2 wins 1 euro, and Player 1 loses 1 euro.

### Genetic Algorithm Approach

1. **Strategy Representation**: Player 1's strategy is represented by a probability function `p(X)` dictating the likelihood of betting based on the drawn number. Similarly, Player 2's strategy is represented by `q(Y)`, the probability of calling based on their drawn number. These functions are represented as step functions (vectors).

2. **Fitness Evaluation**: The fitness of each strategy is calculated based on the expected gain from the game, given the strategies of the opposing player.

3. **Optimization**: The genetic algorithm iteratively refines the strategies to find the optimal balance between betting and calling, considering different betting amounts and game conditions.

### Results and Observations

- **Initial Findings**: In the early iterations (e.g., first 500 iterations), Player 1 tends to bet more aggressively when holding a higher number, while Player 2 initially calls conservatively, resulting in a lower frequency of large losses.

- **Final Strategy**: After 2000 iterations, the optimal strategy for Player 1 stabilizes such that they bet when their number is greater than 0.7 with a probability of 0.9 and refrain from betting otherwise. Player 2's optimal response is to call when their number is greater than 0.5 with a probability of 0.85, folding otherwise.

- **Impact of Bet Amount (B)**: As the bet amount \( B \) increases, both players become more conservative. Player 1 reduces their betting frequency, and Player 2 increases their folding frequency, minimizing the risk of large losses.
