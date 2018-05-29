'''
Description
A two fork tree with n nodes and a root node of 1. Each edge is described by two vertices x[i] and y[i], and the weight of each point is described by d[i].
We define the weights of all nodes from the root node to the leaf node path to be x.
Find the maximum value of x % 1e9+7.

2 <= n <= 10^5
-10^5 <= d[i] <= 10^5
1 <= x[i], y[i] <= n
Have you met this question in a real interview?  
Example
Given x = [1], y = [2], d = [1,1]. return 1.

Explanation:
Maximum product path: 1 -> 2.
Given x = [1,2,2], y = [2,3,4], d = [1,1,-1,2]. return 1000000006.

Explanation:
Maximum product path: 1->2->3.

'''

class Solution:
    """
    @param x: The end points of edges set
    @param y: The end points of edges set
    @param d: The weight of points set
    @return: Return the maximum product
    """
    def getProduct(self, x, y, d):
        # Write your code here
        nodePair = zip(x, y)
        tree = {}
        for p in nodePair:
            tree[p[0]] = tree.get(p[0], []) + [p[1]]
        print(tree)
        self.res = 0
        self.helpFun(tree, 1, d, 1)
        return(self.res)
    
    def helpFun(self, tree, root, d, curr):
        children = tree.get(root, None)
        if children:
            for c in children:
                self.helpFun(tree, c, d, d[root-1]*curr)
        else:
            print(root)
            self.res = max(self.res, (d[root-1]*curr) %1e9+7)
            return
           
        
          
