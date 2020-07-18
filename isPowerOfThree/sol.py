def isPowerOfThree(self, n):
    if n <= 0: return False
    return math.log(n,3)%1 == 0 or 1 - math.log(n,3) % 1 < 0.00000000000001