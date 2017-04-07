"""
找出0到999之间的armstrong number。例如407 == 4^3 + 7 ^3。

"""


def findArmStrongNum():
    res = []
    for i in range(1000):
        if isArmStrong(i):
            res.append(i)
    return(res)
    
def isArmStrong(num):
    numStr = str(num)
    sumNum = 0
    for i in range(len(numStr)):
        sumNum += int(numStr[i]) ** 3
    return(sumNum == num)  


def findArmStrongNum2():
    res = []
    for a in range(10):
        for b in range(10):
            for c in range(10):
                abc = a*100 + b*10 + c
                a3b3c3 = a**3 + b**3 + c**3 
                if abc == a3b3c3:
                    res.append(abc)
    return(res)
                  
        
print(findArmStrongNum())
print(findArmStrongNum2())
