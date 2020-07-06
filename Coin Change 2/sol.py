def change(self, amount, coins):
    lookup = [0 for i in range(amount+1)]
    lookup[0] = 1
    
    for coin in coins:
        for i in range(len(lookup)):
            if i >= coin:
                lookup[i]+=lookup[i-coin]
                
    return lookup[-1]