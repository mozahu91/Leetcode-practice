Classic Algorithm question ever asked.

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

def twoSum(arr,target):
    
    map = {}
    
    for i in range(len(arr)):
        if arr[i] not in map:
            map[target - arr[i]] = i
        else:
            return map[arr[i]],i
            
 arr = [2, 7, 11, 15]
twoSum(arr, 9)

0,1

if we want to return the elements just prefix map with arr
