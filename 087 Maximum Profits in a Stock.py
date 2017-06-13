"""
On-Site Question 1 - SOLUTION
Problem
You've been given a list of historical stock prices for a single day for Amazon stock. The index of the list represents the timestamp, so the element at index of 0 is the initial price of the stock, the element at index 1 is the next recorded price of the stock for that day, etc. Your task is to write a function that will return the maximum profit possible from the purchase and sale of a single share of Amazon stock on that day. Keep in mind to try to make this as efficient as possible.

For example, if you were given the list of stock prices:

prices = [12,11,15,3,10]

Then your function would return the maximum possible profit, which would be 7 (buying at 3 and selling at 10).

Requirements
Try to solve this problem with paper/pencil first without using an IDE. Also keep in mind you should be able to come up with a better solution than just brute forcing every possible sale combination

Also you can't "short" a stock, you must buy before you sell the stock.

Solution
Let's think about a few things before we start coding. One thing to think about right off the bat is that we can't just find the maximum price and the lowest price and then subtract the two, because the max could come before the min.

The brute force method would be to try every possible pair of price combinations, but this would be O(N^2), pretty bad. Also since this is an interview setting you should probably already know that there is a smarter solution.

In this case we will use a greedy algorithm approach. We will iterate through the list of stock prices while keeping track of our maximum profit.

That means for every price we will keep track of the lowest price so far and then check if we can get a better profit than our current max.

Let's see an implementation of this:
"""
def profit(stock_prices):
    if len(stock_prices) < 2:
        raise Exception('Need at least two stock prices!')

    min_stock = stock_prices[0]
    max_profit = 0

    for price in stock_prices:
        min_stock = min(min_stock, price)
        comparision_profit = price - min_stock
        max_profit = max(max_profit, comparision_profit)

    return max_profit

print(profit([10,12,14,12,13,11,8,7,6,13,23,45,11,10]))
39
