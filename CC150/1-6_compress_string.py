'''
Created on Mar 5, 2017

@author: fanxueyi
'''

def compressString(string):
    lastChar = string[0]
    count = 0
    res = []
    for s in string:
        if lastChar == s:
            count += 1
        else:
            res.append(lastChar)
            res.append(str(count))
            count = 1
            lastChar = s
     
    res.append(lastChar)
    res.append(str(count))  
    res = ''.join(res) 
    

    return(res if len(res) < len(string) else string)

print(compressString("aabcccccaaa"))
    
