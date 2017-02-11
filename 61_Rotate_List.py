"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

"""

'''
Created on Feb 10, 2017

@author: fanxueyi
'''

#向右移动的K步，可能会大于链表的长度N，于是乎你需要这么做：

#1、遍历一次链表，得到链表长度N，并且将链表的尾巴连接到头结点上。 
#2、从head开始走n-k%n步的位置那里断开成一个新的链表，那个就是移动后的额结果 
#3、将断开的位置当做新的头结点返回，记得断开的时候别忘了把断开的位置尾巴设置为null（这也是为什么说断开）


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return(head)
        #get the length of the list
        n = 1
        dummy = head
        while dummy.next:
            n += 1
            dummy = dummy.next
        dummy.next = head
        
        k_mod = n- k%n
        p = head
        
        for i in range(k_mod-1):
            p = p.next
        
        #break the lisk    
        head = p.next 
        p.next = None
        return(head)
        
            
