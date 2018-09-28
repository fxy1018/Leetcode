class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        
        首先我们给队列先排个序，按照身高高的排前面，如果身高相同，则第二个数小的排前面。然后我们新建一个空的数组，遍历之前排好序的数组，然后根据每个元素的第二个数字，将其插入到res数组中对应的位置
        """
        
        
        people = sorted(people, key=lambda x:(-x[0], x[1]))
        res = []
        for p in people:
            if not res:
                res.append(p)
            else:
                res.insert(p[1], p)
        return(res)
        
        
