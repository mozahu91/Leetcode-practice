def subsets2(nums):
    res = []
    nums.sort()
    for i in range(1<<len(nums)):
        tmp = []
        for j in range(len(nums)):
            if i&1<<j:
                tmp.append(nums[j])
        if tmp in res:
            i+=1
        else:
            res.append(tmp)
    return res
    
    
    #nums = [1,2,2]
    #subsets2(nums)
    #[[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
