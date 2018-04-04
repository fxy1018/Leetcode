'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

先考慮兩個長方形不交疊的情況，只要單純的計算面積相加即可
AB,EF分別為左下頂點，CD,GH分別為右上頂點，如果A>=G表示第一個長方形在第二個長方形右側而且面積不重疊
同樣方法可判斷兩個長方形其他三個點是否有交疊的情況
如果有交疊的情況發生，使用max(A,E)可以找出交疊正方形的左下頂點，同樣方法可以找出交疊正方形正確位置並計算面積

'''

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        R1 = abs(G-E) * abs(H-F)
        R2 = abs(C-A) * abs(D-B)
        
        if self._isInterset(A, B, C, D, E, F, G, H):
            R3 = 0
        else:
            R3 = abs((max(A,E)-min(C,G))*(max(B,F)-min(D,H)))
            
        
        return(R1+R2-R3)

    def _isInterset(self, A, B, C, D, E, F, G, H):
        return(A>=G or B>=H or C<=E or D<=F)
