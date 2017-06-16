"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

Subscribe to see which companies asked this question.
"""

class Solution(object):
    def majorityElement(self, nums):
        map = {}
        n = len(nums)//3
        for i in nums:
            if i in map:
                map[i] +=1
            else:
                map[i] =1
        res = []
    
        for i,k in map.items():
            if k > n:
                res.append(i)
        
        return res
        
        
