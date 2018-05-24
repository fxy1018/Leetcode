'''
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.

利用栈（Stack）数据结构。

首先将字符串以'\n'进行分割，得到目录/文件的列表，记为parts

然后统计各目录/文件中'\t'的个数，表示当前目录/文件的深度

遍历parts，若栈顶元素的深度不小于parts的深度，则弹出栈顶元素，重复此过程。

然后将新的深度压入栈中，顺便统计当前目录的总长度。

'''

class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        #the input str is pre-order traversal of tree. use stack to record depth
        parts = input.split('\n')
        stack = [(-1,0)]
        res = 0
        for part in parts:
            partList = part.split('\t')
            level = len(partList)-1
            curr = partList[-1]
            while stack[-1][0] >= level:
                stack.pop()
            currPath = stack[-1][1] + len(curr)
            stack.append((level, currPath))     

            if "." in curr:
                res = max(currPath+ level, res)
        return(res)
