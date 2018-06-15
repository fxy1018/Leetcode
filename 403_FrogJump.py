'''
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.

'''
#backtracking time limit exceed
class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        #backtracking
        if not stones:
            return(False)
        if len(stones) == 1:
            if stones[0] == 0:
                return(True)
            else:
                return(False)
        
        if len(stones) >= 2:
            if stones[0] != 0 or stones[1]!=1:
                return(False)
    
        memo= {}
        res = self.helpFun(1, 1, stones, memo)
        return(res)
        
        
    def helpFun(self, pos, preStep, stones, memo):
        if pos == len(stones)-1:
            memo[(pos, preStep)] = True
            return(True)
        
        if (pos, preStep) in memo:
            return(memo[(pos, preStep)])
        res = False
        for i in range(pos+1, len(stones)):
            distance = stones[i] - stones[pos] 
            if distance == preStep or distance == preStep-1 or distance == preStep+1:
                res = res or self.helpFun(i, distance, stones, memo)
        memo[(pos, preStep)] = res
        return(res)
        
#use binary search pass the test
  class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        #backtracking
        if not stones:
            return(False)
        if len(stones) == 1:
            if stones[0] == 0:
                return(True)
            else:
                return(False)
        
        if len(stones) >= 2:
            if stones[0] != 0 or stones[1]!=1:
                return(False)
    
        memo= {}
        res = self.helpFun(1, 1, stones, memo)
        print(memo)
        return(res)
        
        
    def helpFun(self, pos, preStep, stones, memo):
        if pos == len(stones)-1:
            memo[(pos, preStep)] = True
            return(True)
        
        if (pos, preStep) in memo:
            return(memo[(pos, preStep)])
        res = False
        for target in [stones[pos] + preStep-1, stones[pos]+preStep, stones[pos] + preStep+1]:
            findPos = self.binarySearch(pos+1, len(stones), target, stones)
            if findPos != -1:
                res = res or self.helpFun(findPos, target - stones[pos], stones, memo)
        memo[(pos, preStep)] = res
        return(res)
    
    def binarySearch(self, left, right, target, stones):
        while left < right:
            mid = (left+right)//2
            if stones[mid] == target:
                return(mid)
            if stones[mid] < target:
                left = mid +1
            elif stones[mid] > target:
                right = mid-1
        if left != len(stones) and stones[left] == target:
            return(left)
        return(-1)              
