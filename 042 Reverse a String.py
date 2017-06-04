def reverse(s):
    if len(s)<=1:
        return s
    
    else:
        return reverse(s[1:])+s[0]
        
        
reverse('Zahid')
'dihaZ'


def reverString(s):
    index = len(s)
    out = []
    while index:
        index-=1
        out.append(s[index])
    return ''.join(out) 
