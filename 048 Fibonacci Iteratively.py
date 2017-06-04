def fib_iter(n):
    
    # Set starting point
    a = 0
    b = 1
    
    # Follow algorithm
    for i in range(n):
        
        a, b = b, a + b
        
    return a
