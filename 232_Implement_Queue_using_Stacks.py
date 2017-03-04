"""

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).


"""
'''
Created on Mar 4, 2017

@author: fanxueyi
'''

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        stack2 = []
        while len(self.data) != 0:
            stack2.append(self.data.pop())
        stack2.pop()
        while len(stack2) != 0:
            self.data.append(stack2.pop())
        
     

    def peek(self):
        """
        :rtype: int
        """
        stack2 = []
        while len(self.data) != 0:
            stack2.append(self.data.pop())
        peek = stack2[-1]
        while len(stack2) != 0:
            self.data.append(stack2.pop())
        return(peek)
            

    def empty(self):
        """
        :rtype: bool
        """
        return(len(self.data) == 0)


class MyQueue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_push = []
        self.data_pop = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data_push.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.__move()   
        self.data_pop.pop()
      
        
        
    def peek(self):
        """
        :rtype: int
        """
        self.__move()
        return(self.data_pop[-1])
    
    def empty(self):
        """
        :rtype: bool
        """
        return(not self.data_push and not self.data_pop)
    
    
    def __move(self):
        if not self.data_pop:
            while self.data_push:
                num = self.data_push.pop()
                self.data_pop.append(num)  
        
    
    
obj = MyQueue()
obj.push(1)
obj.pop()
