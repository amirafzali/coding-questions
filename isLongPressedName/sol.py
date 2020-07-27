def isLongPressedName(self, name, typed):
    p1 = p2 = 0
    
    while p1 < len(name) and p2 < len(typed):
        if name[p1] != typed[p2]: return False
        
        if p1 == len(name)-1 or name[p1+1] != name[p1]:
            while p2 < len(typed)-1 and typed[p2] == typed[p2+1]:
                p2+=1
        
        p1+=1
        p2+=1
        
    return p1 >= len(name) and p2 >= len(typed)