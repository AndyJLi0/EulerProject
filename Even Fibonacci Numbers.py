def fibonacciNums(n):
    if n <= 0:
        return [0]
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= n:
        nextNum = sequence[-1] +sequence[-2]
        sequence.append(nextNum)

    sequence = list(filter(lambda x: x % 2 == 0, sequence))
    summedSeqeunce = sum(sequence)
    return summedSeqeunce

print(fibonacciNums(4000000))



a, b = 0, 1
sunEvenTerms = 0
while b <= 4000000:
    if b % 2 == 0:
        sunEvenTerms += b
    a, b = b, b + a

print(sunEvenTerms)