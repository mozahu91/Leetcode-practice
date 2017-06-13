"""

We can find the solution with O(log n) complexity
"""
def better_solution(num): 
    if num<0: 
        raise ValueError 
    if num==1: 
        return 1 
    low=0 
    high=1+(num/2) 
    
    while low+1<high: 
        mid=low+(high-low)/2 
        square=mid**2 
        if square==num: 
            return mid 
        elif square<num: 
            low=mid 
        else: high=mid 
            
    return low
