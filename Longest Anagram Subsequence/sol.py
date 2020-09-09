def solve(self, a, b):
    freqa = Counter(a)
    freqb = Counter(b)

    total = 0
    for char,freq in freqa.items():
        if char in freqb:
            total+= min(freqa[char],freqb[char])
            
    return total