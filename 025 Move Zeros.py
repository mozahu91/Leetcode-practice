def moveZeros(arr):
    zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i],arr[zero] = arr[zero],arr[i]
            zero +=1
    return arr
