def missingElement(arr1, arr2):
    arr1.extend(arr2)
    map1 = {}
    for i  in arr1:
        if i in map1:
            map1[i] +=1
        else:
            map1[i] = 1
    
    for k in map1:
        if map1[k] ==1:
            return k
