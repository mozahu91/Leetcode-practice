def searchinRotated(arr, target):
    if not arr:
        return -1
    
    low = 0
    high = len(nums)-1
    
    while low <= high:
        mid = (low+high)//2
        
        if arr[mid] == target:
            return mid
        
        if arr[low] < arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid -1
            else:
                low = mid +1
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid -1
                
    
    return -1
