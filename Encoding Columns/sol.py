def encodeCol(s):
    loop = ord('z')-ord('a')+1
    
    total = 0
    for char in s:
        total = total*loop
        total+=ord(char)-ord('A')+1
        
    return total