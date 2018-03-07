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
        if not head:
            return(head)
            
        
        newNode = RandomListNode(head.label)
        self.visited[head] = newNode
        dummy = head
        out = newNode
        
        while dummy.next:
            new_next_node = RandomListNode(dummy.next.label)
            self.visited[dummy.next] = new_next_node
            newNode.next = new_next_node
            newNode = newNode.next
            dummy = dummy.next
        
        newNode.next = None
        
        dummy = head
        while dummy:
            if not dummy.random:
                self.visited[dummy].random = None
            else:
                self.visited[dummy].random = self.visited[dummy.random]
            dummy = dummy.next
            
        return(out)

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
                
            
                      
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
#method1: use hash
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        
        nodeHash = {None: None}
        q1 = q2 = head
        #cope q1
        while q1:
            newNode = RandomListNode(q1.label)
            nodeHash[q1] = newNode
            q1= q1.next
        #build relationship
        
        while q2:
            nodeHash[q2].next = nodeHash[q2.next]
            nodeHash[q2].random = nodeHash[q2.random]
            q2 = q2.next
            
        return(nodeHash[head])
        
   #method2: copy node follow up the curr node, extra space: O(1)            
    # Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        
        q1 = head
        #replication 
        while q1:
            newNode = RandomListNode(q1.label)
            tmp = q1.next
            q1.next= newNode
            newNode.next= tmp
            q1 = q1.next.next
        
        #get random link
        q2 = head
        while q2:
            if q2.random:
                q2.next.random = q2.random.next
            else:
                q2.next.random = None
            q2 = q2.next.next
        
        #split 
        res = node = head.next
        
        while node and node.next:
            head.next = node.next
            node.next = head.next.next
            head = head.next
            node = node.next
        
        node.next = None
        head.next = None
        return(res)
        
        
        
        
                
        
