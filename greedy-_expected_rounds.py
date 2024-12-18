import numpy as np
import random 

class Alice:
    def __init__(self):
        self.past_play_styles = [1,1]
        self.results = [1,0]         
        self.opp_play_styles = [1,1] 
        self.points = 1

    def play_move(self):
        nB = len(self.results) - self.points
        if self.results[-1] == 1:
            if (nB) / len(self.results) > 6 / 11:
                return 0
            else:
                return 2
        elif self.results[-1] == 0.5:
            return 0
        else:
            return 1
        """
        Decide Alice's play style for the current round.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        
    
    def observe_result(self, own_style, opp_style, result):
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
       
       

class Bob:
    def __init__(self):
        self.past_play_styles = [1,1]
        self.results = [0,1]          
        self.opp_play_styles = [1,1] 
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    alice_move = alice.play_move()
    bob_move = bob.play_move()

    if alice_move == 0 and bob_move == 0:
        p1 = bob.points/(alice.points + bob.points) 
        p3 = 1 - p1
        p2 = 0  
    else:
        p1, p2, p3 = payoff_matrix[alice_move][bob_move]

    outcome = random.choices([1, 0.5, 0], weights=[p1, p2, p3])[0]
    
    alice.observe_result(alice_move, bob_move, outcome)
    bob.observe_result(bob_move, alice_move, 1 - outcome)
   
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """


def estimate_tau(T):
    E_tau = 0
    payoff_matrix = [
        [[1 / 2, 0, 1 / 2], [7 / 10, 0, 3 / 10], [5 / 11, 0, 6 / 11]],  # Alice attacks
        [[3 / 10, 0, 7 / 10], [1 / 3, 1 / 3, 1 / 3], [3 / 10, 1 / 2, 1 / 5]],  # Alice balanced
        [[6 / 11, 0, 5 / 11], [1 / 5, 1 / 2, 3 / 10], [1 / 10, 4 / 5, 1 / 10]]]
    
    num_simulations = 10000
    for _ in range(num_simulations):
        wins_alice = 1
        total_matches = 2
        alice = Alice()
        bob = Bob()

        while (wins_alice != T):
            total_matches += 1
            simulate_round(alice, bob, payoff_matrix)
            if alice.results[-1] == 1:
                wins_alice += 1
        
        E_tau += total_matches / num_simulations

    print(f"Expectation for the greedy strategy is {E_tau}")
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.

    Returns:
        Float: estimated value of E[tau]
    """
    return E_tau

T = 67
estimate_tau(T)
    