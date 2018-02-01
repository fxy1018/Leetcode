'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

'''


'''
Created on Feb 1, 2018

@author: XFan
'''
# Definition for a binary tree node.
from linked_list.common_part_of_two_sorted_list import Solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    #in_order serialize tree, but have problem in deserialize tree, it is hard to find the root
    def serialize2(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return("#")
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            
            else:
                stack.append("#")
                root = stack.pop()
                while root == "#":
                    res.append("#")
                    root = stack.pop()
                
                res.append(str(root.val))
                root = root.right
        res.append("#")
        return("_".join(res))
    
    def serialize(self, root):
        if not root:
            return("#")
        
        stack = [root]
        res = ""
        while stack:
            node = stack.pop()
            if node == "#":
                res += "_#"
            else:
                res = res + "_" + str(node.val)
                
                if node.right:
                    stack.append(node.right)
                else:
                    stack.append("#")
                    
                if node.left:
                    stack.append(node.left)
                else:
                    stack.append("#")
                    
                
        return(res[1:])
             
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "#":
            return(None)
        
        data = data.split("_")
        root = head = TreeNode(data[0])
        stack = [head]
        i = 1
        while i < len(data):
            pre = stack[-1]
            if data[i] != "#" and not pre.left:
                pre.left = TreeNode(data[i])
                stack.append(pre.left)
            elif data[i] != "#" and pre.left:
                pre.right = TreeNode(data[i])
                stack.append(pre.right)
            elif i+1 <len(data) and data[i] == "#" and data[i+1] == "#":
                stack.pop()
                i += 1
            else:
                if data[i] != "#":
                    pre.right = TreeNode(data[i])
                    stack.append(pre.right)
            i += 1
        return(root)
    
root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)

s = Codec()
print(s.serialize(root))
print(s.deserialize(s.serialize(root)).val)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
