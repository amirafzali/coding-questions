def invalidTransactions(self, transactions):
    invalid = set()
    new_transactions = []
    for i in range(len(transactions)):
        copy = transactions[i].split(",")
        copy[1] = int(copy[1])
        copy[2] = int(copy[2])
        new_transactions.append(copy)
        
    for i in range(len(transactions)):
        if new_transactions[i][2] > 1000:
            invalid.add(i)
            
        for j in range(i+1,len(new_transactions)):
            first, second = new_transactions[i], new_transactions[j]
            if first[3] != second[3] and first[0] == second[0] and abs(first[1]-second[1]) <= 60:
                invalid.add(i)
                invalid.add(j)
                
    return [transactions[i] for i in invalid]