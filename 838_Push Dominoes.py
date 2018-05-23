'''
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'


'''
class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        i = 0
        tmp = 0
        res = ""
        while i < len(dominoes) and dominoes[i] == ".":
            tmp += 1
            i += 1
        if i == len(dominoes):
            return(dominoes)
        
        dominoes += "V"
        if dominoes[i] == 'L':
            res += "L" * tmp
            stack = [("L",i)]
        else:
            res += "." * tmp
            stack = [("R", i)]  
        for j in range(i+1, len(dominoes)):
            if dominoes[j] == ".":
                stack.append((".", j))
            elif dominoes[j] == "V":
                if stack[0][0] =="L":
                    res += "".join([d[0] for d in stack])
                else:
                    res += "R"*len(stack)
            else:
                head, pos = stack[0]
                res += head
                currD = dominoes[j]
                for k in range(1, len(stack)):
                    item, itemPos = stack[k]
                    if currD == "L" and head == "R":
                        if itemPos-pos < j-itemPos:
                            res+= "R"
                        elif itemPos-pos > j-itemPos:
                            res += "L"
                        else:
                            res += "."
                    elif currD == "R" and head == "R":
                        res += "R"
                    elif currD == "L" and head == "L":
                        res += "L"
                    else:
                        res += "."
                stack = []
                stack.append((currD, j))  
        return(res)
