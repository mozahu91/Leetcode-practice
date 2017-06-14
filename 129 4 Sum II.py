class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
       
    
        hashtable = {}
    
        for a in A:
            for b in B:
                if a+b in hashtable:
                    hashtable[a+b] +=1
                else:
                    hashtable[a+b] = 1
            #print(hashtable.items())
        count = 0
        for c in C:
            for d in D:
                if -c-d in hashtable:
                    count += hashtable[-c-d]
    
        return count
