# Simple check if one number is prime
def isPrime(self, n):
    if n%2==0: return False
    i = 3
    while i*i <= n:
        if n%i==0: return False
        i+=2
    
    return True

# Get all primes up to n
def countPrimes(self, n):
    if n <= 2: return 0
    
    sieve = set(i for i in range(3, n,2))
    sieve.add(2)
    
    i = 3
    while i*i < n:
        if i in sieve:
            for j in range(i+i, n, i):
                sieve.discard(j)
        i+=2
    
    return len(sieve)