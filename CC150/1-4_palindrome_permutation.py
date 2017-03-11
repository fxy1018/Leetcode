"""



"""


'''
Created on Mar 5, 2017

@author: fanxueyi
'''
import re
def palindromePermutation (string):
#     string = re.sub(r" ", "", string)
    string = string.lower()
    str_arr = [s for s in string] 
    str_set = set(str_arr)
    odd_char = [s for s in str_set if s!= " " and string.count(s)%2 == 1]  
    return(len(odd_char) < 2)

print(palindromePermutation("Tact coa"))