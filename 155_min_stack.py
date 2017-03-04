"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


'''
Created on Mar 4, 2017

@author: fanxueyi
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minV = sys.maxint
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x < self.minV:
            self.minV = x
        self.data.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.data :
            if self.top() == self.minV:
                self.data.pop()
                if self.data :
                    self.minV = min(self.data)
                else:
                    self.minV = sys.maxint
            else: self.data.pop()
    

    def top(self):
        """
        :rtype: int
        """
        if len(self.data)==0:
            return
        else:
            return(self.data[-1])

    def getMin(self):
        """
        :rtype: int
        """
        
        return(self.minV)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




class MinStack2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = [float("Inf")]
        self.min_stack = [float("Inf")]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()
        self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return(self.min_stack[-1])


# Your MinStack object will be instantiated and called as such:
obj = MinStack2()
print (obj.push(2147483646))
print (obj.push(2147483646))
print (obj.push(2147483647))
print (obj.top())
print (obj.pop())
print (obj.getMin())
print (obj.pop())
print (obj.getMin())
print (obj.pop())
print (obj.push(2147483647))
print (obj.top())
print (obj.getMin())
print (obj.push(-2147483648))
print (obj.top())
print (obj.getMin())
print (obj.pop())
print (obj.getMin())


