def letterCombinations(self, digits):
    if not digits: return []
    lookup = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"]
    }
    
    res = []
    
    def getCombos(current, pos):
        if pos >= len(digits):
            res.append("".join(current))
            return
            
        combos = lookup[digits[pos]]
        for i in range(len(combos)):
            current.append(combos[i])
            getCombos(current, pos+1)
            current.pop()
    
    getCombos([],0)
    
    return res