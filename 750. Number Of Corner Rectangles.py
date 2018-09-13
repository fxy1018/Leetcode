'''


'''

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #We ask the question: for each additional row, how many more rectangles are added?
        if not grid:
            return(0)
        connerLocDict = {}
        res = 0
        row = len(grid)
        col = len(grid[0])
        colHasOne = []
    
        for i in range(row):
            pairs = self.getOnePair(grid[i], col)
            if pairs:
                if i == 0:
                    for pair in pairs:
                        connerLocDict[pair] = connerLocDict.get(pair,0)+1
                else:
                    for pair in pairs:
                        if pair in connerLocDict:
                            res += connerLocDict[pair]
                        connerLocDict[pair] = connerLocDict.get(pair,0)+1
        return(res)

    def getOnePair(self, nums, col):
        count = 0
        oneLocs = [i for i in range(col) if nums[i] == 1]
        res = []
        for j in range(len(oneLocs)-1):
            for z in range(j+1, len(oneLocs)):
                res.append((oneLocs[j],oneLocs[z]))           
        return(res)

