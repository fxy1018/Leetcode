"""

"""


'''
Created on Jan 22, 2017

@author: fanxueyi
'''


class Solution(object):
    #use 1-4: represent upper 4 LED
    #use 5-10: repersent down 4 LED
    self.dict = ["1","2","4","8","01","02","04","08","16","32"]
    
    
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        