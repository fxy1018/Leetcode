'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


'''
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return([])
        res = []
        start = 0
        self._helpFun(start, '', s, res, 4)
        return(res)
    
    def _helpFun(self, start,  curr,s, res, group):
        
        if start == len(s):
            if group==0:    
                res.append(curr)
            return
        
        for i in range(1,4):
            if start + i <= len(s):
                if i >1 and s[start]=="0":
                    continue
              
                if int(s[start: (start+i)]) <=255:
                    if group == 4:
                        newCurr = s[start: (start+i)]
                    else:
                        newCurr = curr + "." + s[start: (start+i)]
                    self._helpFun(start+i, newCurr, s, res, group-1)
