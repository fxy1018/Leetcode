"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

"""

'''
Created on Jan 16, 2017

@author: fanxueyi
'''

#method1: 
#先遍历链表一次，拷贝next节点，并将原节点与拷贝过后的复制节点的映射关系用hashmap保存起来。然后再遍历一次链表，通过读取hashmap的映射关系来更新复制节点的random节点。


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# method1
class Solution(object):
    def __init__(self):
        self.visited = {}
    
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        #method1： hash
        if not head:
            return(head)
            
        newHead = RandomListNode(head.label)
        nodeHash = {head:newHead}
        original = head
        copy = newHead
        
        while original and original.next:
            nextNode = RandomListNode(original.next.label)
            copy.next = nextNode
            nodeHash[original.next] = nextNode
            copy = copy.next
            original = original.next
        
        original = head

        while original:
            newNode = nodeHash[original]
            if original.random:
                newNode.random = nodeHash[original.random]
            else:
                newNode.random = None
            original = original.next
        
        return(newHead)
    
#http://yuanhsh.iteye.com/blog/2185974
#method2:
#不需要额外空间，不那么直观。分3步：
#1，复制节点，并将拷贝后的节点放到原节点的后面。
#2，更新所有拷贝节点的random节点：h.next.random = h.random.next。
#3，将原链表与复制链表断开。

      # Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# method2
class Solution(object):
    
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return(head)
        
        dummy = head
        
        while dummy:
            newNode = RandomListNode(dummy.label)
            newNode.next = dummy.next
            dummy.next = newNode
            dummy = dummy.next.next
        
        dummy = head
        
        while dummy:
            if not dummy.random:
                dummy.next.random =None
            else:
                dummy.next.random = dummy.random.next
            dummy = dummy.next.next
        
        out = head.next
        oldList = head
        newList = out
        
        while newList.next:
            oldList.next = newList.next
            oldList = oldList.next
            newList.next = oldList.next
            newList = newList.next
        
        newList.next = None
        oldList.next = None
        
        return(out)
                
            
            
                  
            
            
        