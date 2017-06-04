def fib_seq(n):
    if n==0 or n==1:
        return 1
    
    else:
        return fib_seq(n-1)+fib_seq(n-2)
