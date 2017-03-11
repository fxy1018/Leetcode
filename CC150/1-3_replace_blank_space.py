"""




"""
'''
Created on Mar 5, 2017

@author: fanxueyi
'''

import re
def replaceSpaceOfString(string, length):
    string.strip("")
    string = re.sub(r"\s+", "%20", string)
    return(string) 




print(replaceSpaceOfString("My john Smith", 13))

