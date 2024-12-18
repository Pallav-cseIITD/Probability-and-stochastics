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
        if (nB) / len(self.results) > 15/44:
            return 0
        else:
            return 2
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result

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
            Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        move = random.choice([0, 1, 2])
        return move
        
    
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
    


def monte_carlo(num_rounds):
    bob = Bob()
    alice = Alice()

    payoff_matrix = [
        [[1 / 2, 0, 1 / 2], [7 / 10, 0, 3 / 10], [5 / 11, 0, 6 / 11]], 
        [[3 / 10, 0, 7 / 10], [1 / 3, 1 / 3, 1 / 3], [3 / 10, 1 / 2, 1 / 5]],  
        [[6 / 11, 0, 5 / 11], [1 / 5, 1 / 2, 3 / 10], [1 / 10, 4 / 5, 1 / 10]]]  
   
    for _ in range(num_rounds):
        simulate_round(alice, bob, payoff_matrix)

    print(f"Alices' total score is {alice.points}")
    print(f"Bobs' total score is {bob.points}")
    ans = alice.points / num_rounds
    print(f"Average score of Alices' is {ans}")
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    pass
    

if __name__ == "__main__":
    monte_carlo(num_rounds=100000)