def difSumSquare(n):
    sumOfSquare = 0
    squareOfSum = 0
    for i in range(1, n+1):
        sumOfSquare += i**2
        squareOfSum += i
    
    return(squareOfSum**2 - sumOfSquare)

print(difSumSquare(100))