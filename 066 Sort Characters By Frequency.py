"""
Given a string, sort it in decreasing order based on the frequency of characters.

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""


from collections import Counter, defaultdict
def frequencySort(s):
    c1, c2 = Counter(s), defaultdict(str)
    for k,v in c1.items():
        c2[v] += k*v
    return ''.join(c2[i] for i in range(len(s),0,-1) if i in c2)
