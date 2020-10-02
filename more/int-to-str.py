def numberToWords(self, num: int) -> str:
    first = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
            7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve',
            13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
            18: 'Eighteen', 19: 'Nineteen'}
    second = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: "Seventy", 8: 'Eighty', 9: 'Ninety'}
    
    if num < 20: return first[num]
    
    def break_down(num):
        if num == 0: return ""
        if num < 20: return first[num]
        if num < 100: return (second[num//10] + " " + break_down(num%10)).strip()
        if num < 1000: return (first[num//100] + " Hundred " + break_down(num%100)).strip()
    
    res = ""
    while num > 0:
        if num >= 1e9:
            res+= break_down(num//1e9) + " Billion "
            num%=1e9
        elif num >= 1e6:
            res+= break_down(num//1e6) + " Million "
            num%=1e6
        elif num >= 1e3:
            res+= break_down(num//1e3) + " Thousand "
            num%=1e3
        else:
            res+= break_down(num)
            break
            
    return res.strip()