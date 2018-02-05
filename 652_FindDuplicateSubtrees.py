'''

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1: 
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:
      2
     /
    4
and
    4
Therefore, you need to return above trees' root in the form of a list.

#stratery: postOrder + map,  serialize tree and get subtree string, use subtree string as key, node(substree root) as value. If subtree string 
exist in map, it mean this subtree has been created, so the curr subtree is duplicate, and push the map value to return list.

'''

class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.res =[]
        self.nodeHash = {}
        self.postOrder(root)
        return(self.res)
    
    def postOrder(self, node):
        if not node:
            return("#")
        
        leftStr = self.postOrder(node.left)
        rightStr = self.postOrder(node.right)
        currStr =  str(node.val) + "_" + leftStr + "_" +  rightStr
        if currStr not in self.nodeHash:
            self.nodeHash[currStr] = node
        else:
            if self.nodeHash[currStr] not in self.res:
                self.res.append(self.nodeHash[currStr])
        
        return(currStr)

