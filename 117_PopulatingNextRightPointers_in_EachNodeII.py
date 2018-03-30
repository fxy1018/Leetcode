'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

递推：在第i层的所有next pointer都连接好的情况下，如何连接第i+1层的next pointer?
显然从第i层的最左节点开始依次通过next pointer遍历这一层，同时将他们的children，即第i+1层的节点依次通过next pointer连接起来。连接的时候要分情况处理。

初始情况：对于顶层，只有一个节点root，所以该层连接已经完成。

'''

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    
    #iterative
    def connect(self, root):
        if not root:
            return
        leftMost = root
        while leftMost:
            curr = leftMost
            while curr and not curr.left and not curr.right:
                curr = curr.next
            if not curr:
                return
            leftMost = curr.left if curr.left else curr.right
            pre = leftMost
            while curr:
                if pre == curr.left:
                    if curr.right:
                        pre.next = curr.right
                        pre = pre.next
                    curr = curr.next
                elif pre == curr.right:
                    curr = curr.next
                else: #pre is the child of the previous node of root
                    if not curr.left and not curr.right:
                        curr = curr.next
                        continue
                    pre.next = curr.left if curr.left else curr.right
                    pre = pre.next
                    
