def merge(arr1,arr2):
  m= len(arr1)
  n= len(arr2)
  end= m+n-1
  arr1.extend(arr2)
  
  while l1>=0 and l2>=0:
    if arr2[l2] > arr1[l1]:
      arr1[end]= arr2[l2]
      l2-=1
    else:
      arr1[end] = arr1[l1]
      l1-=1
    end -=1
  
  return arr1
      
