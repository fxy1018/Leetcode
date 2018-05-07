'''
Give a log, consisting of List< String >, each element representing one line of logs. Each line of log information is separated by a space. The first is the ID of the log, followed by the log content.
There are two ways to make content:
1. All consist of letters and spaces.
2. All consist of numbers and spaces.
Now that the logs are sorted, it is required that component 1 be sorted in order of content lexicography and placed at the top, and component 2 should be placed at the bottom and output in the order of input. (Note that the space also belongs to the content, and when the lexicographic order of the composition method 1 is equal, sort according to the dictionary order of log ID., and the guarantee ID is not repeated)

 Notice
The total number of logs entered was n, and n < = 10000.

The length of each line is mi, and mi < = 100.

Have you met this question in a real interview? 
Example
Given

[
    "zo4 4 7",
    "a100 Act zoo",
    "a1 9 2 3 1",
    "g9 act car"
]
, return

[
    "a100 Act zoo",
    "g9 act car",
    "zo4 4 7",
    "a1 9 2 3 1"
]
Explanation:
"Act zoo" < "act car", So the output is as above.
Given

[
    "zo4 4 7",
    "a100 Actzoo",
    "a100 Act zoo",
    "Tac Bctzoo",
    "Tab Bctzoo",
    "g9 act car"
]
, return

[
    "a100 Act zoo",
    "a100 Actzoo",
    "Tab Bctzoo",
    "Tac Bctzoo",
    "g9 act car",
    "zo4 4 7"
]
Explanation:
Because "Bctzoo" == "Bctzoo", the comparison "Tab" and "Tac" have "Tab" < Tac ", so" Tab Bctzoo "< Tac Bctzoo".
Because ' '<'z', so "A100 Act zoo" < A100 Actzoo".

'''

class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        com1 = []
        com2 = []
        
        for log in logs:
            if not self.isCom(log):
                com1.append(log)
            else:
                com2.append(log)
        
        com1 = [self.logParser(log) for log in com1]
        com2 = [self.logParser(log) for log in com2]

        com1 = sorted(com1, key = lambda x: (x[1], x[0]))
        
        return([" ".join(log) for log in com1] + [" ".join(log) for log in com2])

    
    def isCom(self, log):
        logArr = log.split(" ")
        return(logArr[1][0] in "0123456789")
    
    def logParser(self,log):
        logArr = log.split(" ")
        id = logArr[0]
        content = " ".join(logArr[1:])
        return((id, content))

