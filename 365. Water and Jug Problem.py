'''
'''
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        #mx+ny=z,  if z is the muliplier of gcd(x,y)
        if x+y < z:
            return(False)
        
        if x < y:
            x, y = y, x
        gcd = self._gcd(x,y)
        if gcd == 0:
            if z ==0:
                return(True)
            else:
                return(False)
        return(z%gcd== 0)
        
    def _gcd(self, x, y):
        if y == 0:
            return(x)
        return(self._gcd(y, x%y))
