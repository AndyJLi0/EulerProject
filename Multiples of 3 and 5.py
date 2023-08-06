# Initial Solution
cap = 1000
sumSoFar = 0
for x in range(cap):
    if x % 3 == 0 or x % 5 == 0:
        sumSoFar += x
print(sumSoFar)

# solution using list comprehension: make 2 lists incrementing by 5, create set
# to remove any duplicates
setBeforeSum = set(list(range(0, cap, 3)) + list(range(0, cap, 5)))
setSummed = sum(setBeforeSum)

print(setSummed)
