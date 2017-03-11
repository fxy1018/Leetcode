"""

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


"""

'''
Created on Feb 20, 2017

@author: fanxueyi
'''




    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 

class Solution(object):
    #method1: use min heap_priority_queue (priority queue)
    def mergeKLists1(self, lists):
        import heap_priority_queue
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return(None)
        hp = [(n.val,n) for n in lists if n]
        heap_priority_queue.heapify(hp)
        head = curr = ListNode(-1)
    
        while hp:
            (val, node)= heap_priority_queue.heappop(hp)
            curr.next = node
            curr = curr.next
            if node.next:
                heap_priority_queue.heappush(hp, (node.next.val, node.next))

        return head.next
        
        
        