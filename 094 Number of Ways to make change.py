def solution(n, coins):

    arr = [1] + [0]*n

    for coin in coins:
        for i in range(coin, n+1):
            arr[i] += arr[i-coin]

    if n==0:
        return 0
    else:
        return arr[n]

n = 100
coins = [2,3]
print(solution(n, coins))
