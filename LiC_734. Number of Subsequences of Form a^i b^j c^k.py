'''
Given a string, count number of subsequences of the form a^i b^j c^ k, i.e., it consists of i a characters, followed by j b characters, followed by k c characters where i >= 1, j >=1 and k >= 1.

Note: Two subsequences are considered different if the set of array indexes picked for the 2 subsequences are different.

Have you met this question in a real interview? 
Example
Given s = abbc, return 3
Subsequences are abc, abc and abbc

Given s = abcabc, return 7
Subsequences are abc, abc, abbc, aabc, abcc, abc and abc

'''

#method: recursion (TLE)
class Solution:
    """
    @param source: the input string
    @return: the number of subsequences 
    """
    def countSubsequences(self, source):
        # write your code here
        l = len(source)
        self.res = 0
        for i in range(l):
            if source[i] == "a":
                self._helpFun( l, i+1, "a", source)
        return(self.res)
        
    def _helpFun(self, l, start, curr, source):
        if start == l:
            if curr[-1] == "c":
                self.res+=1
            return
        
        if curr[-1] == "a":
            for i in range(start, l):
                if source[i] in "ab":
                    newCurr= curr+source[i]
                    self._helpFun( l, i+1, newCurr, source)
        elif curr[-1]=="b":
            for i in range(start, l):
                if source[i] in "bc":
                    newCurr= curr+source[i]
                    self._helpFun( l, i+1, newCurr, source)
        elif curr[-1] == "c":
            self.res+=1
            for i in range(start, l):
                if source[i] == "c":
                    newCurr= curr+source[i]
                    self._helpFun( l, i+1, newCurr, source)
  '''
  首先要明确一个思路就是说比如当以字符‘c’结尾时有多少种情况是取决于这个c之前的以c结尾的组合数和以b结尾的组合数，当以b结尾时有多少种情况取决于这个b之前的以b结尾的组合数和以a结尾的组合数，当以a结尾时有多少种情况则仅仅取决于这个a之前的以a结尾的组合数，注意这里说以a结尾或者以b结尾的意思并不是真正的结尾，因为结尾一定要以c，这里结尾的意思就是判断到这一位的时候。 
然后我们设以a结尾的组合数为Sa，以b结尾的组合数为Sb，以c结尾的组合数为Sc，那么这里就有三个层层递进的关系了： 
1. Sa => Sa 
2. Sa , Sb => Sb 
3. Sb, Sc => Sc 
我们最后要得到的答案其实就是Sc。 
然后接下仔细分析下这三个关系式的具体实现： 
1. Sa => Sa 
假设一个a前面的以a结尾的组合数为x，那么又来了个a，这个x会变成多少？答案是2x+1，这个2x+1可以其实可以看成 x+x+1，第一份x就是原来的x，即无视掉这个新来的a，第二份x就是对原来的x个组合后面都加上这个新来的a，最后那个1就是忽略掉前面的a，只用新来的这个a，即字符串’a’。 当然这个2x+1也是可以严格计算出来的，假设新的a之前出现过n个字符a，那么x应该等于 2^n-1，那算是这个新来的a之后就出现了n+1个a，那组合数应该就等于 2^(n+1)-1。即x = 2^n-1，设ax+b = 2^(n+1)-1,就可以计算出a=2，b=1。 
2. Sa, Sb => Sb 
假设这时候来了个新的b，这个b前面以a结尾的组合数为Sa，以b结尾的组合数为Sb，那如何去更新Sb的值？很显然 Sb = Sa + 2 * Sb，我们可以再把这个分开来看成 Sb = Sa + Sb + Sb，第一份Sa就是在所有以a结尾的组合后面跟上这个新来的b，第二份Sb可以看成在 所有以b结尾的组合后面跟上这个b，第三份Sb可以看成直接取所有以b结尾的组合，把新的b不要了。 
3. Sb, Sc => Sc 
这个道理跟2一样，同理可得Sc = Sb + 2 * Sc 
  '''
  
  class Solution:
    """
    @param source: the input string
    @return: the number of subsequences 
    """
    def countSubsequences(self, source):
        # write your code here
        
        a = 0
        b = 0
        c = 0
        for i in range(0, len(source)):
            if source[i] == 'a':
                a = 2 * a + 1
            elif source[i] == 'b':
                b = a + 2 * b
            elif source[i] == 'c':
                c = b + c * 2
        return c
