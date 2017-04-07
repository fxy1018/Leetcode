"""

第二个人是给一组输入，第一列是node，第二列是parent，让你建个树返回。例如：
node                parent
2              1
3              1
7              1
4              2
5              2
那么建出来的树就是：
           1
         /        |        \
        2        3        7
       / \        |
     4   5 6


"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = []

def buildTree(arr):
    parents = [t[1] for t in arr]
    children = [t[0] for t in arr]
    
    for i in parents:
        if i not in children:
            rootValue = i
    root = Node[rootValue]
    childParentPair ={}
    valueNodePair = {rootValue: root}
    
    for t in arr:
        childParentPair[t[0]] = t[1]
        childNode = Node(t[0])
        valueNodePair[t[0]] = childNode
        
    for key in childParentPair.keys():
        parent = valueNodePair[childParentPair[key]]
        child = valueNodePair[key]
        parent.children.append(child)
        
    return(root)
    
     

    
    