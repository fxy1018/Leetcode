'''
Created on Mar 25, 2017

@author: fanxueyi
'''



"""
找出数组中重复数字

"""

def findDuplicateNumber(arr):
    """
    input: array
    output: array
    
    """
    res = []
    
    noDupArr = set(arr)
    
    for num in noDupArr:
        if arr.count(num) >= 2:
            res.append(num)
            
    return(res)
        
        
        
        
        
    
    