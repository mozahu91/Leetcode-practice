def oddOccurence(arr):
    map1 = {}
    
    for num in arr:
        if num in map1:
            map1[num] +=1
        else:
            map1[num] =1
    
    odd = []
    for k in map1:
        if map1[k] % 2 ==1:
            odd.append(k)
    
    return odd
        
            
