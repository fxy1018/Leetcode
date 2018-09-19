'''

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

'''

class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        hasOperator = False
        for i in range(len(input)):
            if input[i] in "*-+":
                hasOperator = True
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[(i+1):])
                tmp = self.getTempResult(left, right, input[i])
                res.extend(tmp)
        if not hasOperator:
            return([int(input)])
        return(res)

    def getTempResult(self, left, right, operator):
        res = []
        if operator == "*":
            for l in left:
                for r in right:
                    res.append(l*r)
        if operator == "+":
            for l in left:
                for r in right:
                    res.append(l+r)
        if operator == "-":
            for l in left:
                for r in right:
                    res.append(l-r)
        return(res)
                
