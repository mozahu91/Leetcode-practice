"""Implementation of Shell Sort
The shell sort improves on the insertion sort by breaking the original list into a number of smaller sublists, 
each of which is sorted using an insertion sort. The unique way that these sublists are chosen is the key to the shell sort. 
Instead of breaking the list into sublists of contiguous items, the shell sort uses an increment i, sometimes called the gap, 
to create a sublist by choosing all items that are i items apart.

"""

def shellSort1(arr):
    
    sublist = len(arr)//2
    
    while sublist> 0:
        for start in range(sublist):
        
            gap_insertion_sort(arr, start, sublist)
        
        sublist = sublist//2
        
        
def gap_insertion_sort(arr, start, gap):
    
    for i in range(start+gap, len(arr), gap):
        current = arr[i]
        pos = i
        
        while pos >= gap and arr[pos-gap]> current:
            arr[pos] = arr[pos-gap]
            pos = pos - gap
        
        arr[pos] = current
