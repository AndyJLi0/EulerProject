import math

def nthPrime(n):
    index = 2  # 2nd prime number
    k = 3      # number itself
    while (index <= n):
        if isPrime(k):
            index += 1
        k += 2
    return k-2  # accounts for last +2 from loop
        
def isPrime(n):
    prime = True
    check = 2 
    while ((prime == True) & (check <= math.sqrt(n))):
        if (n % check == 0):
            prime = False
        check += check % 2 + 1
    return prime

print (nthPrime(10001))