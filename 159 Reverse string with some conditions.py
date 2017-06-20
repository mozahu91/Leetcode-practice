"""
This was asked in a Technical interview. Need to remove all the characters in a string which have repeated more that 3 times. Later it was need to reverse the string.
"""

def reverseString(s):
    i=0
    k = []
    while i< len(s)-1:
        if s[i]==s[i+1]==s[i+2]:
            i = i+3
            if s[i]==s[i-1]:
                i +=1
        else:
            k.append(s[i])
            i +=1
    k.append(s[len(s)-1])

    return ''.join(k[::-1])
        #s[::-1]
    #for i in range(len(s)):
s= "aabccccdda"
print(reverseString(s))
