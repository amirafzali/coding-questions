def maxProfit(self, prices):
    profit = start = 0
    if not prices: return profit
    
    for i in range(len(prices)-1):
        current = prices[i]
        bought = prices[start]
        
        if prices[i] > prices[i+1]:
            profit += current - bought
            start = i+1
            
    profit+=prices[-1]-prices[start]
    
    return profit