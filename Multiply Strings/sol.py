def multiply(self, num1, num2):
    if num1 == '0' or num2 == '0': return "0"
    
    toNum = lambda x: ord(x)-48
    total = 0
    
    for i in range(len(num1)):
        for j in range(len(num2)):
            total += toNum(num1[len(num1)-i-1])*toNum(num2[len(num2)-j-1])*(10**(i+j))
            
    return str(total)