def Twosum(lst, target):
    seen = set()
    
    for num in lst:
        num2 = target - num
        
        if num2 in seen:
            return True
        seen.add(num)
    
    return False
    
    
 lst = [5,4,3,1]
Twosum(lst, 6)
True
