def largestPalindromeProject():
    largest = 0
    for y in range(999, 99, -1):
        if y * 999 < largest:
            break
        for x in range(999, 99, -1):
            num = y * x
            if num <= largest:
                break
            reversed = 0
            while num != 0:
                digit = num % 10
                reversed = reversed * 10 + digit
                num //= 10
            if reversed == x * y:
                largest = reversed
    print(largest)


print(largestPalindromeProject())
