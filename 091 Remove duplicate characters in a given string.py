def removeDupicates(str):
    res = []
    seen = set()

    for char in str:
        if char not in seen:
            seen.add(char)
            res.append(char)
    return ''.join(res)
str = "tree traversal"
print(removeDupicates(str))
