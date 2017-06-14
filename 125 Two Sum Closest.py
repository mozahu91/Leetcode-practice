def twoSumClosest(arr, target):
    arr.sort()
    result = arr[0] + arr[1]
    i = 0
    j = len(arr)-1
    while i<j:
        sum1 = arr[i] + arr[j]
            
        if sum1== target:
            return sum1
            
        if abs(sum1 - target) < abs(result - target):
            result = sum1
                
        if sum1 < target:
            j +=1
            
        if sum1 > target:
            j -=1
    
    return result
