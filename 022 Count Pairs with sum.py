def countPairs(arr, x):
    count = 0
    i = 0
    j = i+1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == x:
                count +=1
    print(count//2)
    
    
def countPairs2(arr, sum1):
      
    map1 = {}
    
    for i in range(len(arr)):
        if arr[i] in map1:
            map1[arr[i]]+=1
        else:
            map1[arr[i]] =1
    
    count = 0
    
    for i in range(len(arr)):
        count += map1[sum1 - arr[i]]
        
        if sum1 - arr[i] == arr[i]:
            count -=1 
    
    return count//2
