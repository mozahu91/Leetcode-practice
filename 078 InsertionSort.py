"""
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages:
Simple implementation: Efficient for (quite) small data sets, much like other quadratic sorting algorithms More efficient in practice than most other simple quadratic (i.e., O(n2)) algorithms such as, selection sort or bubble sort
Stable, Method: Insertion
"""

def insertionSort(arr):
    
    for i in range(1,len(arr)):
        currentvalue = i
        position = i
        
        while position>0 and arr[position-1]>currentvalue:
            
            arr[position] = arr[position-1]
            position = position-1
            
        arr[position] = currentvalue
        
    return arr
