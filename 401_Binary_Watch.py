'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

'''
#method1:这种解法利用到了bitset这个类，可以将任意进制数转为二进制，而且又用到了count函数，用来统计1的个数。那么时针从0遍历到11，分针从0遍历到59，然后我们把时针的数组左移6位加上分针的数值，然后统计1的个数，即为亮灯的个数，我们遍历所有的情况，当其等于num的时候，存入结果res中
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num >= 10:
            return[]
        
        res = []
        for i in range(12):
            for j in range(60):
                h = bin(i)[2:].count("1")
                m = bin(j)[2:].count("1")
                if h + m ==num:
                    hour = str(i)
                    minute = str(j)
                    if j < 10:
                        minute = "0" + minute
                    res.append(hour + ":" + minute)
        return(res)
        
