def ChampernowneConstant():
    strDec = str(0.1)
    number = 2
    while (len(strDec) <= 1000002):
        strNumber = str(number)
        strDec = strDec + strNumber
        number += 1
    return int(strDec[2]) * int(strDec[11]) * int(strDec[101]) * int(strDec[1001]) * int(strDec[10001]) * int(strDec[100001]) * int(strDec[1000001]) 
    
print(ChampernowneConstant())

#length needs to be len +2
#acess 100th means [100 +1]