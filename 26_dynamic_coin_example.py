def coinChange(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    min_coins = float("inf")
    for coin in coins:
        res = coinChange(coins, amount - coin)
        if res >= 0:
            min_coins = min(min_coins, 1 + res)

    return min_coins if min_coins != float("inf") else -1
