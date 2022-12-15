'''

The value of an alphanumeric string can be defined as:

The numeric representation of the string in base 10, if it comprises of digits only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs.

'''

class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        maximumValue = 0
        for str in strs:
            maximumValue = max(maximumValue, self.getValueFromStr(str))
        return maximumValue

    def getValueFromStr(self, string):
        letterSet = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        for letter in string:
            if letter not in letterSet:
                return len(string)
        return int(string)
