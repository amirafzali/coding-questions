def palindromeRearranging(inputString):
    freq = Counter(inputString)
    odd = False
    for val in freq.values():
        if val%2==1:
            if odd: return False
            odd = True
            
    return True