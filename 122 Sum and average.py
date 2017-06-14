Sum and Average from a List
Given a list of integers, write a method that returns the sum and average of only the 1st, 3rd, 5th, 7th etc, element.
For example, [1, 2, 3] should return 4 and 2.
The average returned should always be an integer number, rounded to the floor. (3.6 becomes 3.)


def sumavg(arr):
    sum = 0
    n =0
    for i,j in enumerate(arr[::2]):
        sum += j
        n  +=1
    print(sum)
    print(sum//n)
    
Used enumerate to find out the indices while finding out the sum.
