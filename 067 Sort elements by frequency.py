"""
Sort elements by frequency | Set 1
Print the elements of an array in the decreasing frequency if 2 numbers have same frequency then print the one which came first.
"""

from collections import defaultdict

def frequentElements(arr):
    d = {}
    
    for i in arr:
        if i in d:
            d[i] +=1
        else:
            d[i] =1
    
    c = (sorted(d,key=d.get, reverse = True))
    
    res = []
    for i in c:
        res.extend([i]*d[i])
    
    return res
    
