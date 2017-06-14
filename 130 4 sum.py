Given an array of numbers arr and a number S, find 4 different numbers in arr that sum up to S.

Write a function that gets arr and S and returns an array with 4 indices of such numbers in arr, or null if no such combination exists.
Explain and code the most efficient solution possible, and analyze its runtime and space complexity.


Algorithm to solve this question:

1. Assign a dictionary d, Add the pair sum into the dictionary appending indexes if it exits, else just assigning their indices
2. Iniliaze a result to set
3. loop for keys in d,val = tar - get, 

def fourSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if len(nums) < 4:
            return -1

        #nums.sort()
        d = dict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                val = nums[i] + nums[j]
                if val in d:
                    d[val].append((i,j))
                else:
                    d[val] = [(i,j)]
        
        #print(d.items())
        res = []
        for k in d:
            #print(k)
            val = target - k
            if val in d:
                vlist = d[val]
                klist = d[k]
    
        for (i,j) in vlist:
            for (l,m) in klist:
                    ilist = [i,j,l,m]
                    #if len(set(ilist)) != len(ilist):
                    #        continue
                    mylist = [i,j,l,m]
                    mylist.sort()
                    res.append( tuple(mylist) )
        
        return res
