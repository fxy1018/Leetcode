'''

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false

'''

class Solution:
#method1: stack, like trim the subtree  不断的砍掉叶子节点。最后看看能不能全部砍掉。已例子一为例，：”9,3,4,#,#,1,#,#,2,#,6,#,#” 遇到x # #的时候，就把它变为 #
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        #method1: stack:
        stack=[]
        preorder = preorder.split(",")
        for node in preorder:
            stack.append(node)
            while len(stack) > 2 and stack[-1] == "#" and stack[-2] == "#":
                stack.pop()
                stack.pop()
                if stack[-1] != "#":
                    stack.pop()
                    stack.append("#")
                else:
                    return(False)
            
        return(len(stack)==1 and stack[-1]=="#")
        
        
   #method2: In a binary tree, if we consider null as leaves, then

all non-null node provides 2 outdegree and 1 indegree (2 children and 1 parent), except root
all null node provides 0 outdegree and 1 indegree (0 child and 1 parent).
Suppose we try to build this tree. During building, we record the difference between out degree and in degree diff = outdegree - indegree. When the next node comes, we then decrease diff by 1, because the node provides an in degree. If the node is not null, we increase diff by2, because it provides two out degrees. If a serialization is correct, diff should never be negative and diff will be zero when finished.
#我们在遍历的时候，计算diff = outdegree – indegree. 当一个节点出现的时候，diff – 1，因为它提供一个入度；当节点不是#的时候，diff+2(提供两个出度) 如果序列式合法的，那么遍历过程中diff >=0 且最后结果为0.
   
   def isValidSerialization2(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        diff = 1
        for i in preorder:
            diff -=  1
            if diff < 0:
                return(False)
            if i != "#":
                diff += 2
        return(diff == 0)
