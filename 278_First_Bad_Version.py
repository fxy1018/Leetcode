'''
Created on Jan 5, 2017

@author: fanxueyi
'''
#You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

#Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

#You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


#binary search 

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l_b = 1
        r_b = n
        
        while l_b < r_b :
            mid = (l_b+r_b)//2
            
            if (isBadVersion(mid)==False):
                l_b = mid+1
            else:
                r_b = mid
                
        return(l_b)
            
          
          
 # The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #binary search
        low = 1
        high = n
        
        while low <= high:
            mid = (low+high)/2
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    high = mid - 1
                else:
                    return(mid)
            else:
                if isBadVersion(mid+1):
                    return(mid+1)
                else:
                    low = mid + 1 
                    
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #binary search

        low = 1
        high = n
        
        while low <= high:
            mid = (low+high)/2
            if isBadVersion(mid) == False:
                low = mid + 1  
            else:
                high = mid - 1   
        return(low)
                
        
