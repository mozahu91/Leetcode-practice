Getting a Different Number

Given an array arr of n unique non-negative integers, how can you most efficiently find a non-negative integer that is not in the array?

Your solution should return such an integer or null if arr contains all possible integers.
Analyze the runtime and space complexity of your solution.


Piegon Hole concept:

1. First initiliaze an array which is greater than the size of the array
2. if the len(arr) = max interger +1 return null, it contains everything
3. the Initilized array appended with zeros throughout
4. Loop the first array, through (n-1), particular index increment by 1, if it contains duplicates, convert to se
5. Loop through the result array from 1 to n, since 0 is neiter positive nor negative..

def getAnotherNumber(arr):
    n = len(arr)
    l = n+1
    arr2 = [0] * l
    for i in range(n-1):
        num = arr[i]
        arr2[num] += 1
    for i in range(1,n):
        if arr2[i] ==0:
            return i
