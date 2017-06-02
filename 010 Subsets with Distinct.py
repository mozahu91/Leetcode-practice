def subsets(nums):
    res = []
    nums.sort()
    for i in range(1<<len(nums)):
        tmp = []
        for j in range(len(nums)):
            if i&1<<j:
                tmp.append(nums[j])
        res.append(tmp)
    return res
    
    
    
#nums = [1,2,3]
#subsets(nums)
#[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
