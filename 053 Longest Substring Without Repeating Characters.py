"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
def longestSubstring(s):
    start = 0
    maxlength = 0
    map = {}
    
    for i in range(len(s)-1):
        if s[i] in map and start <= map[s[i]]:
            start = map[s[i]]+1
        else:
            maxlength = max(maxlength, i- start +1)
    
    return maxlength
