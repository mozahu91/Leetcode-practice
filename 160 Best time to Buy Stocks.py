"""
Asked in an interview, return the indices of buy date and sell date for maximum profit to be generated.
"""
arr = [12, 5, 6, 8, 9, 15, 14, 14]
#arr = [7, 1, 5, 3, 6, 4]
def maxProfit(arr):
    if len(arr)<2:
        raise Exception("Need atleast two stock_prices")

    min_price = arr[0]
    max_profit = 0
    map1 = {}
    profit = []
    for price in range(len(arr)):
        if arr[price] < min_price:
            min_price = price
        if arr[price] - min_price > max_profit:
            max_profit = arr[price] - arr[min_price]
            profit.append(max_profit)
            map1[max_profit] = (min_price,price)

    buySell = max(profit)
    return map1[buySell]

print(maxProfit(arr))
