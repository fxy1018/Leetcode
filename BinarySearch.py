
'''
Created on Feb 18, 2017

@author: fanxueyi
'''


def binarySearch(arr, target):
    arr = sorted(arr)
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2 # get the interger
        if arr[mid ]< target:
            left = mid+1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return(True)
    return(False)


print(binarySearch([3,1,2,6,4], 8))