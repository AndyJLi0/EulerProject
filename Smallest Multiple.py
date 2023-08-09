import math


def smallestMultiple(n):
    mult = 0    # smallset multiple
    number = n  # tries every multiple of n
    while mult == 0: 
        works = True    
        for i in range(1, n+1):   # test every number [1,n]
            if (number % i != 0): 
                works = False     # set false when a number fails
        
        if (works == False):
            number += n           # try again with next multiple
        else: mult = number       # break loop if successful
    
    return mult

# print(smallestMultiple(20))

def isPrime(p):
  prime = 1
  check = 2
  while (prime == 1) and (check <= math.sqrt(p)):
    if (p % check == 0):
      prime = 0   # not prime
    check += check % 2 + 1 
  return prime == 1 # prime

def f(n):
  if (n == 1):
    return 1
  else:
    product = 2 ** int(math.log(n) / math.log(2))  
    k = 3
    while (k <= n):
      if (isPrime(k)):
        product *= k ** int(math.log(n) / math.log(k))
      k += 2
    return product

## the LCM of n is the product of every prime number x^(log(x)/log(n)) where x < n

print(f(100))

