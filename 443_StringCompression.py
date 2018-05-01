'''
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.

'''

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        lastCharIndex = -1
        char = chars[0]
        for i in range(1, len(chars)):
            if chars[i] != char:
                chars[lastCharIndex + 1] = char
                lastCharIndex += 1
                lastCharIndex = self.helpFun(count, lastCharIndex, chars)
                count = 1
                char = chars[i]
            else:
                count += 1
                
        chars[lastCharIndex + 1] = char
        lastCharIndex += 1
        lastCharIndex = self.helpFun(count, lastCharIndex, chars)
        return(lastCharIndex+1)
    
    def helpFun(self, count, lastCharIndex, chars):
        if count > 1:
            tmp = []
            while count > 0:
                div,mod = divmod(count, 10)
                tmp.append(str(int(mod)))
                count = (count-mod)//10
            while tmp:
                chars[lastCharIndex + 1] = tmp.pop()
                lastCharIndex += 1
        return(lastCharIndex)
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        point = 0
        pre = chars[0]
        curr = 1
        count = 1
        
        while curr <= len(chars) :
            if curr == len(chars):
                chars[point] = pre
                point += 1
                if count != 1:
                    count = [c for c in str(count)]
                    for c in count:
                        chars[point] = c
                        point += 1
                break
                
            if chars[curr] == pre:
                count += 1
            else:
                chars[point] = pre
                pre = chars[curr]
                point += 1
                if count != 1:
                    count = [c for c in str(count)]
                    for c in count:
                        chars[point] = c
                        point += 1
                count = 1
            curr += 1
        return(point)
                        
                    
                
        
        
        
        
