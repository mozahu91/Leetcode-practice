"""

Finds the position of max, replaces the last item with that
Class Sorting algorithm Data structure Array Worst-case performance О(n2) Best-case performance О(n2) Average performance О(n2) Worst-case space complexity О(n) total, O(1) auxiliary
Not Stable, Method: Selection
"""

def selectionSort(arr):
    for fillslot in range(len(arr)-1,0,-1):
        positionOfMax = 0
            
        for location in range(1, fillslot+1):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location
    
        arr[fillslot], arr[positionOfMax] = arr[positionOfMax], arr[fillslot]
    
    return arr
    
arr = [5,3,7,2]
selectionSort(arr)
