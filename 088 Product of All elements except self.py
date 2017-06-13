"""
On-Site Question 2 - SOLUTION
Problem
Given a list of integers, write a function that will return a list, in which for each index the element will be the product of all the integers except for the element at that index

For example, an input of [1,2,3,4] would return [24,12,8,6] by performing [2×3×4,1×3×4,1×2×4,1×2×3]

Requirements
You can not use division in your answer! Meaning you can't simply multiply all the numbers and then divide by eahc element for each index!

Try to do this on a white board or with paper/pencil.

Solution
If you look at the list above with the multiplication you'll notice we are repeating multiplications, such as 2 times 3 or 3 times 4 for multiple entries in the new list.

We'll want to take a greedy approach and keep track of these results for later re-use at other indices. We'll also need to think about what if a number is zero!

In order to find the products of all the integers (except for the integer at that index) we will actually go through our list twice in a greedy fashion.

On the first pass we will get the products of all the integers before each index, and then on the second pass we will go backwards to get the products of all the integers after each index.

Then we just need to multiply all the products before and after each index in order to get the final product answer!

Let's see this in action:
"""

def index_prod(arr):

    output = [None] * len(arr)
    product = 1
    i =0

    while i < len(arr):
        output[i] = product
        product *= arr[i]
        i+=1

    product =1
    i = len(arr)-1

    while i>=0:
        output[i] *= product
        product *= arr[i]
        i -=1

    return output

print(index_prod([1,2,3,4]))
