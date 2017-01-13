
#Implement regular expression matching with support for '.' and '*'.

'''
Created on Jan 13, 2017

@author: fanxueyi
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        s = "0" + s
        p = "0" + p
        print(s,p)
        nrow,ncol = len(s), len(p)
        T = [['']*(ncol) for i in range(nrow)]
        
        #initialize the matrix first row and first column. Pattern are as col, and String are as row
        T[0][0] = True 
        for i in range(1,nrow):
            T[i][0] = False
        
        for j in range(1,ncol):
            if j>=2 and p[j] == "*" and T[0][j-2] == True:
                T[0][j] = True
            else:
                T[0][j] = False        
         
        
        for i in range(1,nrow):
            for j in range(1,ncol):
                
                #if last chars are equal, see the truth table of i-1, j-1
                if p[j]==s[i] or p[j] == ".":
                    T[i][j] = T[i-1][j-1]
                    
                #if last pattern is *, first to check if * represent 0, then not 0
                elif p[j]=="*":
                    if j >= 2 :
                        if T[i][j-2] == True:
                            T[i][j] = T[i][j-2]
                        elif p[j-1] == "." or s[i]==p[j-1]:
                            T[i][j] = T[i-1][j]
                else:
                    T[i][j]=False
        print(T)
        return(T[nrow-1][ncol-1]==True)
                    

                