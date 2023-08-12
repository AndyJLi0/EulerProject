def nthDivisorsTriangularNumber(n):
    index = 500
    while True:
        factors = 0
        triNum = index*(index +1) // 2
        limit = int(triNum**0.5) + 1
        for y in range(1, limit):
            if (triNum % y == 0):
                factors += 2
        if limit**2 == triNum:
            factors -= 1
        if (factors > n):
            return triNum
        index += 1

print(nthDivisorsTriangularNumber(500))
