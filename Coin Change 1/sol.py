# Bottom up
def coinChange(self, coins, amount):
    if not coins: return -1

    ways = [float('inf') for i in range(amount+1)]
    ways[0] = 0
    
    for coin in coins:
        for i in range(1,len(ways)):
            if i >= coin: ways[i] = min(ways[i], ways[i-coin]+1)

    return ways[-1] if ways[-1] != float('inf') else -1

# Top down
def coinChange(self, coins, amount):
    mem = {0:0}
    for i in range(1,amount+1):
        self.needed(coins, i, mem)

    return mem[amount] if mem[amount] <= amount else -1

def needed(self, coins, amount, mem):
    total = float('inf')
    if amount in mem: return mem[amount]
    
    for coin in coins:
        if coin <= amount:
            total = min(total, 1+self.needed(coins, amount-coin, mem))
    
    mem[amount] = total
    return mem[amount]