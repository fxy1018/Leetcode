class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_final = self.getBackString(S)
        t_final = self.getBackString(T)
        return(s_final == t_final)
    
    def getBackString(self, s):
        j = 0
        while s[j] == "#": 
            j+=1
        stack = [s[j]]
        for i in range(j+1, len(s)):
            if s[i] != "#":
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
        return(stack)
               
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i = len(S)-1
        j = len(T)-1
        skipS = 0
        skipT = 0
        while i >=0 or j>=0:
            while i>=0:
                if S[i] == "#":
                    skipS +=1
                    i-=1
                elif skipS > 0:
                    skipS-=1
                    i-=1
                else:
                    break
                    
            while j >=0:
                if T[j] == "#":
                    skipT +=1
                    j-=1
                elif skipT > 0:
                    skipT-=1
                    j-=1
                else:
                    break
            if i>=0 and j>=0 and S[i] != T[j]:
                return(False)
            if (i>=0) != (j>=0):
                return(False)
            i -= 1
            j -= 1
        return(True)
