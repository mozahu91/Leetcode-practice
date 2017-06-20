def add(a,b):
    if b==0:
        return a
    s = a^b
    c = (a&b) << 1
    return add(s,c)
