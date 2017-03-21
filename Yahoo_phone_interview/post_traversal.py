"""

tree post traversal

"""

'''
Created on Mar 19, 2017

@author: fanxueyi
'''

#recursive

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postTraveralRecur(root):
    if not root:
        return
    print(root.val)
    postTraveralRecur(root.left)
    postTraveralRecur(root.right)
    
def postTraveralIter1(root):
    #two stack
    if not root:
        return(root)
    
    stackIn = [root]
    stackOut = []

    while stackIn:
        node = stackIn.pop()
        stackOut.append(node)
        if node.left:
            stackIn.append(node.left)
        if node.right:
            stackIn.append(node.right)
    
    while stackOut:
        print(stackOut.pop().val)

def postTraveralIter2(root):
    #one stack
    if not root:
        return(root)
    
    stack = [root]
    pre = root
    
    while stack:
        curr = stack[-1]
        if curr.left and curr.left != pre and curr.right != pre:
            stack.append(curr.left)
        elif curr.right and curr.right != pre:
            stack.append(curr.right)
        else:
            print(stack.pop().val)
            pre = curr
            
def morrisPost(root):
    if not root:
        return(root)
    
    currNode = root
    while currNode:
        if not currNode.left:
            currNode = currNode.right
        else:
            leftChild = currNode.left
            while leftChild.right and leftChild.right != currNode:
                leftChild = leftChild.right
            if not leftChild.right:
                leftChild.right = currNode
                currNode = currNode.left
            else:
                leftChild.right = None
                printEdge(currNode.left)
                currNode = currNode.right
    printEdge(root)
    

def printEdge(node):
    tail = reverseEdge(node)
    curr = tail
    while curr:
        print(curr.val)
        curr = curr.right
    reverseEdge(tail)

def reverseEdge(node):
    pre = None
    next = None
    while node:
        next = node.right
        node.right = pre
        pre = node
        node = next
    return(pre)
    

    
    
    
        
            

