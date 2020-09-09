# Bottom up
def coinChange(self, coins, amount):
    mem = {0:0}
    
    for change in range(1, amount+1):
        mem[change] = float('inf')
        for coin in coins:
            if change-coin in mem:
                mem[change] = min(mem[change], mem[change-coin]+1)
                
    return mem[amount] if mem[amount] <= amount else -1

# Top down
def coinChange(self, coins, amount):
    mem = {}
    
    def search(current):
        if current == 0: return 0
        if current in mem: return mem[current]
        
        fewest = float('inf')
        for coin in coins:
            if current >= coin:
                fewest = min(fewest, 1+search(current-coin))
        
        mem[current] = fewest
        return fewest
    
    res = search(amount)
    return res if res <= amount else -1