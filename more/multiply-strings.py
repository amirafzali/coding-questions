def multiply(self, num1, num2):
    total = 0
    for i in range(len(num2)):
        for j in range(len(num1)):
            bottom = num2[len(num2)-i-1]
            top = num1[len(num1)-j-1]
            
            total+= (ord(bottom)-48)*(ord(top)-48)*10**(i+j)
    
    return str(total)