"""
Performance[edit] Bubble sort has worst-case and average complexity both О(n2), where n is the number of items being sorted. There exist many sorting algorithms with substantially better worst-case or average complexity of O(n log n). Even other О(n2) sorting algorithms, such as insertion sort, tend to have better performance than bubble sort. Therefore, bubble sort is not a practical sorting algorithm when n is large.
The only significant advantage that bubble sort has over most other implementations, even quicksort, but not insertion sort,
is that the ability to detect that the list is sorted efficiently is built into the algorithm. When the list is already sorted 
(best-case), the complexity of bubble sort is only O(n). By contrast, most other algorithms, even those with better
average-case complexity, perform their entire sorting process on the set and thus are more complex.
However, not only does insertion sort have this mechanism too, but it also performs better on a list that is substantially
sorted (having a small number of inversions). Bubble sort should be avoided in the case of large collections. 
It will not be efficient in the case of a reverse-ordered collection.

"""

def bubbleSort(arr):
    
    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            if arr[k]>arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    
    return arr
