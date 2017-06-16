import collections
d = collections.OrderedDict()
def firstchar(s):
    for char in s:
        if char in d:
            d[char] +=1
        else:
            d[char] =1
    
    for char in range(len(s)):
        if d[s[char]]==1:
            return char
    
    return -1


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        for i in range(len(s)):
            c = s[i]
            if s.count(c)==1:
                return i

        return -1

    def firstUniqChar2(self, s):

        from collections import Counter
        sc = Counter(s)
        for i in range(len(s)):
            c = s[i]
            if sc.get(c,0)==1:
                return i

        return -1
