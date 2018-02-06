'''
Created on Feb 1, 2018

@author: XFan
'''
#TreeNode
class TreeNode(object):
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None
#BFS:
def bfs(root):
    if not root:
        return(root)
    
    queue = [root]
    
    while queue:
        node = queue[0]
        queue = queue[1:]
        
        print(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

#recursion
class Recursion(object):
    def preOrder(self, root):
        if not root:
            return
        
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
        
    def inOrder(self, root):
        if not root:
            return
        
        self.preOrder(root.left)
        print(root.val)
        self.preOrder(root.right)
        
    def postOrder(self, root):
        if not root:
            return
        
        self.preOrder(root.left)
        self.preOrder(root.right)
        print(root.val)


class Interation(object):
    #root, left, right
    def preOrder(self, root):
        if not root:
            return
        
        stack = [root]
        while stack:
            node = stack.pop()
            print(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
    def inOrder(self, root):
        #left, root, right
        if not root:
            return
        
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left 
            else:
                root = stack.pop()
                print(root.val)
                root = root.right
                
                
    
    def postOrder1(self, root):
        #left, right, root
        #use two stack
        #reverse the preorder:  root, right, left
        if not root:
            return
        
        stack1 = [root]
        stack2 = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        while stack2:
            print(stack2.pop().val)
            
    
    def postOrder2(self, root):
        #left, right, root
        #use one stack
        #two point, curr: current node,  pre: preprint node,  pre print node can help us node the stage of curr node
        if not root:
            return 
        
        stack = [root]
        curr = pre = None
        
        while stack:
            curr = stack[-1]
            if curr.left and pre != curr.left and pre != curr.right:
                stack.append(curr.left)
                
            elif curr.right and pre != curr.right:
                stack.append(curr.right)
                
            else:
                print(stack.pop().val)
                pre = curr
        
class Morris(object):
    def preOrder(self, root):
        if not root:
            print("root is null")
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                if tmp.right == root:
                    tmp.right = None
                    root = root.right
                else:
                    print(root.val)
                    tmp.right = root
                    root = root.left   
            else:
                print(root.val)
                root = root.right
    
    
    def inOrder(self, root):
        if not root:
            print("root is null")
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                if tmp.right == root:
                    print(root.val)
                    tmp.right = None
                    root = root.right
                else:
                    tmp.right = root
                    root = root.left   
            else:
                print(root.val)
                root = root.right
            
            
    def postOrder(self, root):
        if not root:
            print("root is null")
        head = root
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right != root:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = root
                    root = root.left
                else:
                    tmp.right = None
                    self.printRightEdge(root.left)
                    root = root.right
            else:
                root = root.right
                
        self.printRightEdge(head)
    
    def printRightEdge(self, node):
        head = self.reverseList(node)
        tmp = head 
        while tmp:
            print(tmp.val)
            tmp = tmp.right
        self.reverseList(head)
        
    def reverseList(self, node):
        pre = None
        while node:
            nextNode = node.right
            node.right = pre
            pre = node
            node = nextNode
        return(pre)
            
        

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)

s=Morris()
print("preOrder")
s.preOrder(root)
print("inOrder")
s.inOrder(root)
print("postOrder")
s.postOrder(root)
