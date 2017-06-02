"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

def climbStairs(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
