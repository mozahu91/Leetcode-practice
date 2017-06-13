"""
Implementation of Merge Sort
Merge sort is a recursive algorithm that continually splits a list in half. 
If the list is empty or has one item, it is sorted by definition (the base case).
If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. 
Once the two halves are sorted, the fundamental operation, called a merge, is performed.
Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list.


"""

def mergeSort(arr):

    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i< len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i+=1
            else:
                arr[k] = righthalf[j]
                j+=1

            k+=1
        while i<len(lefthalf):
            arr[k]= lefthalf[i]
            i+=1
            k+=1

        while j< len(righthalf):
            arr[k]=righthalf[j]
            j+=1
            k+=1
    return arr

arr = [11,2,5,4,7,6,8,1,23]
print(mergeSort(arr))
