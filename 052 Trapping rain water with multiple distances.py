def trap(arr, distances):
    new_array = []
    for i in range(len(arr)-1):
        new_array.append(arr[i])
        new_array.extend([0]*distances[i])
    new_array.append(arr[len(arr)-1])
    print(new_array)
    
    height, left, right, water = [], 0, 0, []
    for i in new_array:
        left = max(left, i)
        height.insert(0,left)
    #print(height)
    #height.reverse()
    print(height)
    sum =0   
    for n, i in enumerate(reversed(new_array)):
        right = max(right, i)
        res = min(height[n], right) - i
        sum += res
        if res ==0:
            water.append(sum)
            sum =0
    return max(water)
