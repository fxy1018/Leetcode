'''
A string, each character representing a scene. Between two identical characters is considered to be a continuous scene. For example: abcda, you can think of these five characters as the same scene. Or acafghbeb can think of two aca and beb scenes. If there is a coincidence between the scenes, then the scenes are combined. For example, abcab, where abca and bcab are coincident, then the five characters are considered to be the same scene. Give a string to find the longest scene.

Example
Given str = "abcda", return 5.

Explanation:
The longest scene is "abcda".
Given str = "abcab", return 5.

Explanation:
The longest scene is "abcab".

'''

class Solution:
    """
    @param str: The scene string
    @return: Return the length longest scene
    """
    def getLongestScene(self, str):
        # Write your code here
        #interval merge
        posHash = {}
        res = 1
        interval = []
        for i in range(len(str)):
            if str[i] not in posHash:
                posHash[str[i]] = [i, i]
            else:
                posHash[str[i]][1] = i
                res = max(res, (i-posHash[str[i]][0]+1))
        interval = [posHash[key] for key in posHash]         
        interval = sorted(interval, key=lambda x: x[0])
        
        pre = interval[0]
        for i in interval[1:]:
            if i[0] < pre[1]:
                pre = [pre[0], max(i[1], pre[1])]
                res = max(res, (pre[-1]-pre[0]+1))
            else:
                pre = i
        return(res)
