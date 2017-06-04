"""
This uses the concept of Dynamic Programming
"""

def fib_dyn(n):
    
    if n==0 or n==1:
        return n
    
    cache = [None]*(n+1)
    
    if cache[n] != None:
        return cache[n]
    
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    
    return cache[n]
