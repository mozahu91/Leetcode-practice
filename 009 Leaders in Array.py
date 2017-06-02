def leaders(arr):
    max_from_right = arr[len(arr)-1]
    print(max_from_right)
    
    for i in range(len(arr)-2,0,-1):
        if max_from_right < arr[i]:
            print(arr[i])
            max_from_right = arr[i]
            
  
  #arr = [16, 17, 4, 3, 5, 2]
  #leaders(arr)
  
