def maxProfit(self, prices):
    if not prices: return 0
    smallest = largest = prices[0]
    potential = 0
    
    for i in range(len(prices)):
        current = prices[i]
        
        if current < smallest:
            potential = max(potential, largest-smallest)
            smallest=largest=current
            
        elif current > largest:
            largest = current
            
    return max(potential, largest-smallest)