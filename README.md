**MindGames Chess Strategies**

**Overview**

This project focuses on solving a series of problems based on a probabilistic game between two players, Alice and Bob, who play multiple rounds of chess. In this game, each player can choose their strategy in each round (aggressive, balanced, or defensive), and the outcome depends on both players’ choices. The objective is to analyze and compute optimal strategies for Alice under different scenarios involving Bob's behavior.

The solution employs mathematical derivations, probabilistic calculations, and Monte Carlo simulations to model and solve the problems.

**Problem Statement**

Alice and Bob play a chess game, with outcomes determined by their strategies. Alice's goal is to maximize her score over a series of rounds. The game has three strategic styles for each player:

-   **Aggressive**
-   **Balanced**
-   **Defensive**

Each pair of strategies has associated probabilities for Alice winning, drawing, or losing. The probabilities change based on the players' past performances or chosen strategies. Points are awarded as follows:

-   **Win:** +1 point
-   **Draw:** +0.5 points
-   **Loss:** 0 points

The assignment is broken into three parts:

**1. Fixed Strategies (Both Players Always Attack)**

-    Calculate the probability that Alice wins a specific number of matches and Bob wins another specific number of matches after TTT rounds.
-    Define a random variable for Alice’s score per round and compute the expectation (EEE) and variance (VarVarVar) of Alice’s total score over TTT rounds.

**2. Performance-Dependent Strategy for Bob**

Bob’s strategy depends on his performance in the previous round:

-   **Win:** Bob plays defensively.
-   **Draw:** Bob plays balanced.
-   **Loss:** Bob plays aggressively.
    -    Determine Alice's optimal strategy to maximize her points in a single round and validate the solution using Monte Carlo simulation.
    -    Investigate whether Alice should always use the greedy (optimal single-round) strategy to maximize her total points. Identify scenarios where a non-greedy strategy might outperform and validate with simulations.
    -    Estimate the expected number of rounds (E[τ]E[\\tau]E[τ]) required for Alice to achieve a target number of wins using the greedy strategy, using Monte Carlo simulation.

**3. Randomized Strategy for Bob**

Bob now plays randomly, choosing each strategy (aggressive, balanced, defensive) with equal probability.

-    Determine Alice's optimal strategy to maximize her points in a single round when Bob plays randomly. Validate using simulations.
-   Calculate the expected total points Alice will gain over TTT rounds when Bob plays randomly. Derive the mathematical expectation and validate using Monte Carlo simulations.

**Approach to Solving**

**Mathematical Derivations**

For questions requiring probabilistic analysis:

1.  Calculate the probabilities of outcomes based on the strategy combinations and given matrices.
2.  Derive the expected values and variances using summations over the given probabilities.

**Monte Carlo Simulations**

For questions involving simulations:

1.  Implement randomized trials to replicate the game dynamics over 10510\^5105 iterations.
2.  Use simulations to validate theoretical results or explore complex cases where mathematical derivation is infeasible.
