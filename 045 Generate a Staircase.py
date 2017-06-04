def staircase(n):
    k = n-1
    for stairs in range(n):
        print(' '*k,'#'*stairs)
        k -=1
    print('#'*n)
    
    
   #
  ##
 ###
####
