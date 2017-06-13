def findSquareRoot(num):
    if num <0:
        raise ValueError
    if num ==1:
        return 1

    for k in range(1+(num//2)):
        if k**2 == num:
            return k
        elif k**2 > num:
            return k-1

    return k
print(findSquareRoot(14))


O(n)
