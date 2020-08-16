def reverseInParentheses(inputString, reverse = False):
    res = []
    i = 0
    while i < len(inputString):
        if inputString[i] == "(":
            opened = 1
            start = i+1
            i+=1
            while opened:
                if inputString[i] == "(":
                    opened+=1
                if inputString[i] == ")":
                    opened-=1
                if opened: i+=1
            
            for char in reverseInParentheses(inputString[start:i], True):
                res.append(char)
        else:
            res.append(inputString[i])
        i+=1
        
    if reverse: return "".join(res[::-1])
    return "".join(res)