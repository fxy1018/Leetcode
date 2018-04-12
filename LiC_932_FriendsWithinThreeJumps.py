'''
Given two array a and b, a[i] and b[i] are friends. And then given two query arrays c and d, find whether c[i] and d[i] are friends within three jumps.(i.e A and B are friends, B and C are friends, so B is a one-jump friend of A and C is a two-jumps friend of A)

 Notice
The length of all arrays do not exceed 1000.
If there is more than one friend relationship chain, calculate the relationship of least jumps.

Example
Given a = [1,2], b = [2,3], c = [1], d = [3], return [1].

Explanation:
1 → 2 → 3 ，3 is a two-jumps friend of 1.
Given a = [1,2,3,4], b = [2,3,4,5], c = [1,1], d = [4,5], return [1,0].

Explanation:
1 → 2 → 3 → 4 → 5，4 is a three-jumps friend of 1, 5 is a four-jumps friend of 1.
'''

class Solution:
    """
    @param a: The a tuple
    @param b: The b tuple
    @param c: the c tuple
    @param d: the d tuple
    @return: The answer
    """
    #graph + bfs(shorest distance)
    def withinThreeJumps(self, a, b, c, d):
        # Write your code here
        friends = {}
        for i in range(len(a)):
            if a[i] not in friends:
                friends[a[i]] = [b[i]]
            else:
                friends[a[i]].append(b[i])
            if b[i] not in friends:
                friends[b[i]] = [a[i]]
            else:
                friends[b[i]].append(a[i])

        tofind = zip(c,d)
        
        res = []
        for pair in tofind:
            if pair[0] not in friends and pair[1] not in b:
                res.append(0)
            else:
                res.append(self._helpFun(pair, friends))
        return(res)
    
    def _helpFun(self, pair, friends):
        node1 = pair[0]
        node2 = pair[1]
        
        queue = [(node1, 0)]
        visited = set([])
        
        while queue:
            node, level = queue[0]
            visited.add(node)
            queue = queue[1:]
            if node == node2 and level <= 3:
                return(1)
            if level > 3:
                return(0)
            if node in friends:
                newNodes = [ (n, level+ 1) for n in friends[node]]
            else:
                newNodes = []
            for n in newNodes:
                if n not in visited:
                    queue.append(n)
        return(0)
            
            
