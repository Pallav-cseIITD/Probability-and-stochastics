"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

# Problem 1a
def calc_prob(alice_wins, bob_wins):
    dp=[[0 for i in range(bob_wins+1)] for j in range (alice_wins +1)]
    dp[1][1] =1
    for i in range(1, alice_wins + 1):
        for j in range(1, bob_wins + 1):
            if i > 1:  # Alice wins
                dp[i][j] = mod_add(dp[i][j], mod_multiply(dp[i-1][j], mod_divide(j ,(i-1+j))))
            if j > 1:  # Bob wins
                dp[i][j] = mod_add(dp[i][j], mod_multiply(dp[i][j-1] , mod_divide(i, (i+j-1))))

    return dp[alice_wins][bob_wins]
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    
# Problem 1b (Expectation)      
def calc_expectation(t):
    ans= 0
    for i in range(1,t):
        z = i - (t-i)
        ans = mod_add(ans, mod_multiply(z, calc_prob(i, t-i)))
    return ans
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
   

# Problem 1b (Variance)
def calc_variance(t):
    ans = 0
    for i in range(1,t):
        z = i - (t-i)
        ans = mod_add(ans, mod_multiply(mod_multiply(z,z), calc_prob(i, t-i)))
    return ans
    """
    Returns:
        The variance of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    
    
if __name__ == "__main__":
    # last four digits of my entry number are 1067 --> 19 67
    alice_wins = 19
    bob_wins = 67
    ans1a = calc_prob(alice_wins, bob_wins)
    print(f"The answer of question 1a is {ans1a}")

    T = 67
    expect = calc_expectation(T)
    var = calc_variance(T)
    print(f"The answer of expectation is {expect}")
    print(f"The answer of Variance is {var}")
