Question 4: Find the Second Most Frequent Number
Given a list of integers, return the number that appears second most frequently.

As an example, the function would receive:
[0, 1, 2, 2, 2, 2, 1, 0, 5, 1]
And returns:
1


import collections

def finder2(arr1): 
    # Using default dict to avoid key errors
    d=collections.defaultdict(int) 
    
    # Add a count for every instance in Array 1
    for num in arr1:
        d[num]+=1 
    del d[max(d, key=d.get)]
    return max(d, key=d.get)
