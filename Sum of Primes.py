import math

def sumOfPrimes(n):
    total = 2 
    for i in range (3, n + 1):
        if (isPrime(i)):
            total += i
    return total

def isPrime(i):
    Prime = True
    check = 2
    while (Prime == True) and (check <= math.sqrt(i)):
        if (i % check == 0) :
            Prime = False
        check += check % 2 + 1
    return Prime

print(sumOfPrimes(2000000))