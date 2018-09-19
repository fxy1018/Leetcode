class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    """
    @param numbers: the given list
    @param node1: the given node1
    @param node2: the given node2
    @return: the distance between two nodes
    """
    def bstDistance(self, numbers, node1, node2):
        # Write your code here
        if node1 not in numbers or node2 not in numbers or not numbers:
            return(-1)
        root = self.builtBST(numbers)
        return(self.getDistance(root, node1, node2))
    
    def builtBST(self, numbers):
        root = Node(numbers[0])
        for i in range(1, len(numbers)):
            self.addNode(root, numbers[i])
        return(root)
    
    def addNode(self, root,num):
        pre = None
        while root:
            if num > root.val:
                if not root.right:
                    root.right = Node(num)
                    return
                else:
                    root = root.right
            if num < root.val:
                if not root.left:
                    root.left = Node(num)
                    return
                else:
                    root = root.left
        
    def getDistance(self, root, node1, node2):
        while root:
            if root.val > max(node1, node2):
                root = root.left
            
            elif root.val < min(node1, node2):
                root = root.right
            
            else:
                break
        return(self.getDistanceHelp(root, node1) + self.getDistanceHelp(root, node2))
    
    def getDistanceHelp(self, root, node):
        if root.val ==node:
            return(0)
        if root.val > node:
            return(1+self.getDistanceHelp(root.left, node))
        if root.val < node:
            return(1+self.getDistanceHelp(root.right, node))
        
