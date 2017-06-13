"""
A quick sort first selects a value, which is called the pivot value. Although there are many different ways to choose the pivot value, we will simply use the first item in the list. The role of the pivot value is to assist with splitting the list. The actual position where the pivot value belongs in the final sorted list, commonly called the split point, will be used to divide the list for subsequent calls to the quick sort.
Method: Partitioning algorithm Space: logn worst: n^2 Best and avergaeL n log n Stable avialable, inplace is not

"""

def qquickSort(arr):
    
    quickSorthelp(arr, 0, len(arr)-1)
    return arr

def quickSorthelp(arr, first, last):
    if first < last:
        splitpoint = partition(arr,first, last)
        quickSorthelp(arr, first, splitpoint-1)
        quickSorthelp(arr, splitpoint+1, last)


def partition(arr, first, last):
    pivotValue = arr[first]
    
    leftmark = first +1
    rightmark = last
    
    done = False
    
    while not done:
        
        while leftmark <= rightmark and arr[leftmark] <= pivotValue:
            leftmark +=1
        
        while arr[rightmark] >= pivotValue and rightmark >= leftmark:
            rightmark -=1
        
        if rightmark < leftmark:
            done = True
        else:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]
    
    arr[first],arr[rightmark] = arr[rightmark], arr[first]
    
    return rightmark
