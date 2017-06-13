"""
Find Minimum in Sorted Rotated Array
Question:

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

"""
def findMin(arr):

    left = 0
    right = len(arr)-1

    while left < right and arr[left] >= arr[right]:
        mid = (left+right)//2
        if arr[mid]>arr[right]:
            left = mid +1
        else:
            right = mid -1

    return arr[left]
arr = [4,5,6,7,0,1,2]
print(findMin(arr))
