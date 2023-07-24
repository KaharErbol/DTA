def coin_change(coins, amount):
    dp = [float('inf') for _ in range(amount+1)]
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], 1 + dp[i - c])

    return -1 if dp[amount] == float('inf') else dp[amount]


print(coin_change([1,2,5], 11))

"""
coins: 1, 2, 3
amount: 4
dp:     0   1   2   3   4   
coins:  0   1   1   1   2
"""