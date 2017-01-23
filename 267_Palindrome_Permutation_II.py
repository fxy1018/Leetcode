"""


Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

Hint:

If a palindromic permutation exists, we just need to generate the first half of the string.
To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.

"""




'''
Created on Jan 23, 2017

@author: fanxueyi
'''

class Solution(object):
    def __init__(self):
        self.result=[]
        self.n = 0
        self.created = []
    
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        str_dict ={}
        for i in s:
            if i not in str_dict:
                str_dict[i] = 1
            else:
                str_dict[i] += 1
        new_s = ""
        count_odd = 0
        mid = ""

#check whether this can generate permutation, 
#if it can, get half of the s

        for key in str_dict:
            if count_odd < 2:
                if str_dict[key] % 2 ==1:
                    mid = key
                    count_odd += 1
                    print(count_odd)
                new_s += key*(str_dict[key]//2)
        if count_odd>=2:
            return([])
        
        #backtracking method to generate all permutation
        self.n = len(new_s)
        comb = ""
        self.helpFun(new_s, 0, comb)
        
        for i in range(len(self.result)):
            self.result[i] = self.result[i]+mid+self.result[i][::-1]
        
        return(self.result)
    
    def helpFun(self, s, index, comb):
        if index == self.n:
            self.result.append(comb)
            return
        
        for i in range(len(comb)+1):
            if i==0:
                new_comb = s[index]+comb
            elif i==len(comb):
                new_comb = comb + s[index]
            else:
                new_comb = comb[0:i]+s[index]+comb[i:]
            
            if new_comb not in self.created:
                self.created.append(new_comb)
                self.helpFun(s, index+1, new_comb)
    


s = Solution()
print(s.generatePalindromes("as"))
