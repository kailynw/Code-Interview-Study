def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    rs = [amount + 1] * (amount + 1)
    rs[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i >= c:
                rs[i] = min(rs[i], rs[i - c] + 1)

    if rs[amount] == amount + 1:
        return -1
    return rs[amount]

if __name__ == "__main__":
    coins = [1, 3, 5, 2, 8]
    amount = 4
    print(coinChange(coins, amount))