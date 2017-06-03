def productExceptSelf(arr):
    p =1
    n = len(arr)
    output = []
    for i in range(n):
        output.append(p)
        p *= arr[i]
    p =1
    for i in range(n-1,-1,-1):
        output[i] *=p
        p *= arr[i]
    
    return output
