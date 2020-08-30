def decodeString(self, s):
    res = []
    i = 0
    while i < len(s):
        if s[i].isalpha(): 
            res.append(s[i])
        else:
            start = i
            while s[i] != '[':
                i+=1
            times = int(s[start:i])
            i+=1
            start = i
            balance = 1
            while balance != 0: 
                if s[i] == ']': balance-=1
                if s[i] == '[': balance+=1
                if balance!=0: i+=1
            body = self.decodeString(s[start:i])
            for j in range(times): res.append(body)

        i+=1
    return "".join(res)