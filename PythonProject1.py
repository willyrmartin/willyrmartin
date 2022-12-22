numList = []
n = 0
sumNum = 0
for n in range(10):
    numList.append(n)
    sumNum = int(numList[n-1]) + n
    prevNum = int(numList[n-1])
    print("Current Number: ", end = " ")  
    print(numList[n], end = " "),
    print("Previous Number :", end = " "),
    print(prevNum, end = " "),
    print("Sum :", end = " "),
    print(sumNum)
   
    