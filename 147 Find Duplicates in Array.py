"""
Given an array of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and using only constant memory space.

For example, let n be 7 and array be {1, 2, 3, 1, 3, 6, 6}, the answer should be 1, 3 and 6.

"""

def findDupicates(arr):
    
    map = {}
    
    for i in arr:
        if i in map:
            map[i] +=1
        else:
            map[i] =1
    duplicates = []
    for k in map:
        if map[k]>1:
            duplicates.append(k)
    
    return duplicates
