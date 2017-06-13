"""
If the rotated sorted array could contain duplicates? Is your algorithm still O(log n) in

runtime complexity?

Solution:

For case where AL == AM == AR, the minimum could be on AM’s left or right side (eg,

[1, 1, 1, 0, 1] or [1, 0, 1, 1, 1]). In this case, we could not discard either subarrays and

therefore such worst case degenerates to the order of O(n).

"""

def minSortedduplicate(arr):

    left = 0
    right = len(arr)-1

    while left < right and arr[left] >= arr[right]:
        mid = (left+right)//2

        if arr[mid] > arr[right]:
            left = mid+1
        elif arr[mid] < arr[left]:
            right = mid
        else:
            left +=1

    return arr[left]

arr = [1, 1, 1, 0, 1]
print(minSortedduplicate(arr))
