'''

Description:

Count the number of prime numbers less than a non-negative number, n.

'''

class Solution(object):

###time out for large number###
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = []
        for i in range(0, n):
            if self.isPrime(i):
                out.append(i)
        return(len(out))
        
        
    def isPrime(self,n):
        if n <=1:
            return(False)
        elif n <= 3:
            return(True)
        elif n%2 == 0 or n%3==0:
            return(False)
        i = 5
        while i**2 <= n:
            if n % i ==0 or n % (i+2) == 0:
                return(False)
            i  = i +6
        return(True)
        
 class Solution2(object):
 #use a list to record prime (index as number)
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return(0)
        
        prime = [True] * n
        
        prime[0] = prime[1] = False
        
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                prime[i*i:n:i] = [False] * len(prime[i*i:n:i])
        
        return(sum(prime))
         
