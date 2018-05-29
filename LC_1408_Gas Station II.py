'''
A car is driving on a straight road and it has original units of gasoline.
There are n gas stations on this straight road, and the distance between the i-th gas station and the starting position of the car is distance[i] unit distance, which can add apply[i] unit gasoline to the car.
The vehicle consumes 1 unit of gasoline for every 1 unit traveled, assuming that the car's fuel tank can hold an unlimited amount of gasoline.
The distance from the starting point of the car to the destination is target. Will the car arrive at the destination? If it can return the minimum number of refuelings, it will return -1.

Example
Given target = 25, original = 10, distance = [10,14,20,21], apply = [10,5,2,4], return 2.

Explanation:
Refuel at the 1st and 2nd gas stations.
Given target = 25, original = 10, distance = [10,14,20,21], apply = [1,1,1,1], return -1.

Explanation:
The car can't reach the destination.

'''

class Solution:
    """
    @param target: The target distance
    @param original: The original gas
    @param distance: The distance array
    @param apply: The apply array
    @return: Return the minimum times
    """
    def getTimes(self, target, original, distance, apply):
        pass
        # Write your code here
        apply = [0] + apply
        distance = [0] + distance
        self.res = len(apply) + 1
        
        self.helpFun(original, 0, 0,  target, original, distance, apply)
        
        if self.res == len(apply) + 1 :
            return(-1)
        return(self.res)
        
        
    def helpFun(self, fuel, currPos, c, target, original, distance, apply):
        if distance[currPos] + fuel >= target:
            self.res = min(self.res, c)
            return
        if distance[currPos] + fuel + apply[currPos] >= target:
            self.res = min(self.res, c+1)
            return
        
        #unfuel in currPos
        for i in range(currPos+1, len(distance)):
            if fuel >= distance[i] - distance[currPos]:
                newFuel = fuel - (distance[i] - distance[currPos])
                self.helpFun(newFuel, i, c, target, original, distance, apply)
            else:
                break
            
        #add fuel
        if currPos > 0:
            for i in range(currPos+1, len(distance)):
                if fuel + apply[currPos] >= distance[i] - distance[currPos]:
                    newFuel = fuel+apply[currPos] - (distance[i] - distance[currPos])
                    self.helpFun(newFuel, i, c+1, target, original, distance, apply)
                else:
                    break
