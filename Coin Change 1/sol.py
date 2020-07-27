def coinChange(self, coins, amount):
    if not coins: return -1

    ways = [float('inf') for i in range(amount+1)]
    ways[0] = 0
    
    for coin in coins:
        for i in range(1,len(ways)):
            if i >= coin: ways[i] = min(ways[i], ways[i-coin]+1)

    return ways[-1] if ways[-1] != float('inf') else -1