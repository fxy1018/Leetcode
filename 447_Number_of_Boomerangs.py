'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]


'''

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p in points:
            distHash= {}
            for q in points:
                dist = self.getDist(p, q)
                distHash[dist] = distHash.get(dist,[])
                distHash[dist].append(q)
            for dist in distHash:
                l = len(distHash[dist])
                if  l > 1:
                    res += l*(l-1)
        return(res)
                
    
    def getDist(self, pair1, pair2):
        return((pair1[0] - pair2[0])**2 + (pair1[1] - pair2[1])**2)
