"""

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:

An easy approach is to sort the array first.
What are the possible values of h-index?
A faster approach is to use extra space.

"""


'''
Created on Feb 8, 2017

@author: fanxueyi
'''


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        #method1: 排个序，然后从引用高到低遍历，如果引用数大于论文数，则加１．其时间复杂度为O(n log n)，即快速排序的时间．

        citations.sort()
        h_index = 0
        n = len(citations)

        for i in range(n-1, -1,-1):
            if citations[i] > h_index:
                h_index += 1
            
        return(h_index)
    
    
        #method2: 用空间换时间可以将时间复杂度降为O(n).

#这种做法的思路是根据这个index的范围是[0, array.size()]，因此我们只需要从高到低统计引用数比当前index大的论文数量．

#如果当前论文数量比index大了说明，这个index就是h-index，也就是至少有index篇论文，且引用数不低于index．此时我们就可以返回答案了
    
    
    