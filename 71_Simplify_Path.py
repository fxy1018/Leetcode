"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

"""




'''
Created on Feb 10, 2017

@author: fanxueyi
'''


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack  = []
        path = path.split("/")
        #print(path)
        stack.append(path[0])
        
        for i in range(1,len(path)):
            if path[i] == "" or path[i] == ".":
                continue
            elif path[i] == "..":
                if not stack:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(path[i])
        #print(stack)
        if not stack:
            return("/")
        if len(stack)==0 and stack[0]=="":
            return("/")
        out = "/".join(stack)
        if out[0] != "/":
            return("/"+ out )
        return(out)
    
    
        #method2: simplified
        
        path = [p for p in path.split("/") if p != "." and p != ""]
        stack = []
        for p in path:
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return("/" + "/".join(stack))
            
        
                
            
            
s = Solution()
print(s.simplifyPath("/..."))