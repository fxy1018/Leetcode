"""

DFS: pre-order, in-order, post-order  (recrusive and iterative)
Morris Travesal


"""


'''
Created on Mar 11, 2017

@author: fanxueyi
'''


class Node(object):
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None
        
        
class TreeTravesal(object):
    def preOrderRecur(self, head):
        if not head:
            return
        print(head.val)
        self.preOrderRecur(head.left)
        self.preOrderRecur(head.right)
    
    def inOrderRecur(self,head):
        if not head:
            return
        self.inOrderRecur(head.left)
        print(head.val)
        self.inOrderRecur(head.right)
    
    def postOrderRecur(self,head):
        if not head:
            return
        self.postOrderRecur(head.left)
        self.postOrderRecur(head.right)
        print(head.val)
    
    
    def preOrderIter(self,head):
        if not head:
            return
        
        stack = []
        stack.append(head)
        while stack:
            node = stack.pop()
            print(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
    def inOrderIter(self,head):
        if not head:
            return 
        stack = []
        while stack or head:
            if head:
                stack.append(head)
                head = head.left
            else:
                head = stack.pop()
                print(head.val)
                head = head.right
    
    #two stacks postOrderIter
    def postOrderIter(self,head):
        if not head:
            return
        
        stack1 = []
        stack2 = []
        stack1.append(head)
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            print(stack2.pop().val)  
        
    
    #one stack postOrderIter:
    def postOrderIter2(self,head):
        if not head:
            return
        
        stack = [head]
        pre = head
        while stack:
            curr = stack[-1]
            if curr.left and pre !=  curr.left and pre != curr.right:
                stack.append(curr.left)
            elif curr.right and pre != curr.right:
                stack.append(curr.right)
            else:
                print(stack.pop().val)
                pre = curr
        
    
    def morrisPre(self,head):
        if not head:
            return
        
        curr = head
        while curr:
            temp = curr.left
            if temp:
                while temp.right and temp.right != curr:
                    temp = temp.right
                if not temp.right:
                    temp.right = curr
                    print(curr.val)
                    curr = curr.left 
                else:
                    temp.right = None
                    curr = curr.right
                 
            else:
                print(curr.val)
                curr = curr.right
    
    
    def morrisIn(self,head):
        if not head:
            return
        
        curr = head
        while curr:
            temp = curr.left
            if temp:
                while temp.right and temp.right != curr:
                    temp = temp.right
                if temp.right == curr:
                    temp.right = None
                    print(curr.val)
                    curr = curr.right
                else:
                    temp.right = curr
                    curr = curr.left  
            else:
                print(curr.val)
                curr = curr.right
                
    
    def morrisPost(self,head):
        if not head:
            return
        
        curr = head
        while curr:
            temp = curr.left
            if temp:
                while temp.right and temp.right != curr:
                    temp = temp.right
                if temp.right == curr:
                    temp.right = None
                    self.printEdge(curr.left)
                    curr = curr.right
                else:
                    temp.right = curr
                    curr = curr.left  
            else:
                curr = curr.right
        
        self.printEdge(head)
                
    def printEdge(self,head):
        tail = self.reverseEdge(head)
        curr = tail
        while curr:
            print(curr.val)
            curr = curr.right
        
        self.reverseEdge(tail)
         
    def reverseEdge(self, head):
        pre = None
        next = None
        while head:
            next = head.right
            head.right = pre
            pre = head
            head = next
        return pre
    
            
        
s = TreeTravesal()
head = Node(4)
head.left = Node(2);
head.right = Node(6);
head.left.left = Node(1);
head.left.right = Node(3);
head.right.left = Node(5);
head.right.right = Node(7);

# s.preOrderRecur(head)
# s.preOrderIter(head)
# s.inOrderIter(head)
# s.inOrderRecur(head)
# s.postOrderRecur(head)
# s.postOrderIter(head)


# s.morrisPre(head)
# s.morrisIn(head)
s.morrisPost(head)
    

        
        
            
    

