'''
Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.

'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        #recursion
        if not s :
            return(NestedInteger())
        if s[0] != "[":
            return(NestedInteger(int(s)))
        if len(s) <=2 : 
            return(NestedInteger())
        
        res = NestedInteger()
        
        start = 1 #record new level start position
        count = 0 #record whether it is same level.
        for i in range(1, len(s)):
            if count == 0 and (s[i] == "," or i == len(s)-1):
                res.add(self.deserialize(s[start: i]))
                start = i + 1
            elif s[i] == "[": 
                count += 1
            elif s[i] == "]":
                count -= 1
                
        return(res)
       
            
    class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        #iteration
        if not s :
            return(NestedInteger())
        if s[0] != "[":
            return(NestedInteger(int(s)))
        if len(s) <=2 : 
            return(NestedInteger())
        stack = []
        i = 0
        sign = 1
        num = 0
        while i < len(s):
            if s[i] =="[":
                stack.append(s[i])
                i += 1
            elif s[i] in "-1234567890":
                if s[i] == "-":
                    sign = -1
                    i += 1
                while s[i] in "1234567890":
                    num = 10*num + int(s[i])
                    i += 1
                stack.append(num*sign)
                sign = 1
                num = 0
            elif s[i] == "]":
                tmpArr = []
                while stack[-1] != "[":
                    tmpArr.append(NestedInteger(stack.pop())) 
                stack.pop()
                stack.append(tmpArr[::-1])
                i += 1
            else:
                i += 1
        return(stack[0]) 
        
        
        
