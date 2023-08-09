def fibNumbLength(n):
    numb1 = 1
    numb2 = 1
    newNumber = 0
    index = 2
    while (len(str(numb2)) != n) :
        newNumber = numb1 + numb2
        index += 1
        #prepare for next loop
        numb1 = numb2
        numb2 = newNumber
    return index

print(fibNumbLength(1000))
