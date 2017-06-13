"""
Problem
Create a function that takes in a list of unsorted prices (integers) and a maximum possible price value,
and return a sorted list of prices

We can actually solve this problem by using a counting sort. Basically a counting sort works well when you know the range of integer values you will
have ahead of time.

"""


def solution(unsorted_prices, max_price):
    princes_to_counts = [0]*(max_price+1)

    for price in unsorted_prices:
        princes_to_counts[price] +=1

    sorted_price = []

    for price, count in enumerate(princes_to_counts):
        for k in range(count):
            sorted_price.append(price)

    return sorted_price
print(solution([4,6,2,7,3,8,9],9))
