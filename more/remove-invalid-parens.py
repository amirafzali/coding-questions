def removeInvalidParentheses(self, s):
    status = [0,0]
    for i in range(len(s)):
        if s[i] == "(":
            status[0]+=1
        elif s[i] == ")" and status[0] > 0:
            status[0]-=1
        elif s[i] == ")":
            status[1]+=1
    
    res = []
    def search(pos,current,balance,o,c):
        if balance == 0 and pos==len(s):
            res.append(current[:])     
        if pos == len(s):
            return
            
        if s[pos] != ")" and s[pos] != "(":
            current.append(s[pos])
            search(pos+1,current,balance,o,c)
            current.pop()
            
        elif s[pos] == "(":
            if o > 0:
                search(pos+1,current,balance,o-1,c)
            current.append(s[pos])
            search(pos+1,current,balance+1,o,c)
            current.pop()
            
        elif s[pos] == ")":
            if balance > 0:
                current.append(s[pos])
                search(pos+1,current,balance-1,o,c)
                current.pop()
            if c > 0:
                search(pos+1,current,balance,o,c-1)
    
    search(0,[],0,status[0],status[1])
    
    res = ["".join(e) for e in res]
    return list(set(res))