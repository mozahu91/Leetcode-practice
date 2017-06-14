his can also be solved without using the dictionary method in Python

O(n) complexity
O(1) space

def twoSum(arr, target):
    
    left, right = 0 ,len(arr)-1
    
    while left < right:
        sum1 = arr[left] + arr[right]
        
        if sum1 == target:
            return [left+1, right+1]
        
        elif sum1 < target:
            left +=1
        
        else:
            sum1 > target
            right -=1
