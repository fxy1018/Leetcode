'''
Given n keys(numbered from 1 to n) and m locks(numbered from 1 to m). When the number of the lock can be divisible by the number of the key, the lock can be opened/closed. Initially, all locks are locked, then use all keys to unlock all locks, find the number of locks which is opened in the end.

 Notice
1 <= m, n <= 10^5
Example
Given n = 1, m = 1, return 1.

Explanation:
The lock numbered 1 has been unlocked.
Given n = 2, m = 5, return 3.

Explanation:
The locks numbered 1,3,5 have been opened.

'''
class Solution:
    """
    @param n: the number of keys
    @param m: the number of locks
    @return: the numbers of open locks
    """
    def unlock(self, n, m):
        # Write your code here
        #O(mn)
        res = [0 for _ in range(m)]
        
        for i in range(1, m+1):
            res[i-1] = self._isOpen(n,i)
        
        return(sum(res))
    
    def _isOpen(self, n, i):
        count = 0
        for j in range(1, min(n,i)+1):
            if i%j == 0:
                count += 1
        return(~count %2 ==0)
