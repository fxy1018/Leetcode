'''
Created on Feb 19, 2017

@author: fanxueyi
'''

def findMaxValue(arr):
    max = arr[0] + 0
    min = arr[0] +0

    for i in range(len(arr)):
        if max < arr[i]+i:
            max = arr[i]+i
        if min > arr[i]+i:
            min = arr[i]+i
    return(max - min)

def findMaxValue2(arr):
    if len(arr) <2 :
            return(0)

    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[i] + i)

    p1 = 0
    p2 = 1
    max_value = -2**31
    while p2 < len(new_arr):
        max_value = max(max_value, new_arr[p2]-new_arr[p1])
        if new_arr[p2] < new_arr[p1]:
            p1 = p2
        p2 +=1
    return(max_value)

print(findMaxValue2([6,3,1,-1,-3,-5]))