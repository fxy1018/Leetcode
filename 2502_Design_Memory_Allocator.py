'''
You are given an integer n representing the size of a 0-indexed memory array. All memory units are initially free.

You have a memory allocator with the following functionalities:

Allocate a block of size consecutive free memory units and assign it the id mID.
Free all memory units with the given id mID.
Note that:

Multiple blocks can be allocated to the same mID.
You should free all the memory units with mID, even if they were allocated in different blocks.
Implement the Allocator class:

Allocator(int n) Initializes an Allocator object with a memory array of size n.
int allocate(int size, int mID) Find the leftmost block of size consecutive free memory units and allocate it with the id mID. Return the block's first index. If such a block does not exist, return -1.
int free(int mID) Free all memory units with the id mID. Return the number of memory units you have freed.


'''

class Allocator(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.memory = [0] * n
        self.n = n
        self.locationSumArr = [i for i in range(n, 0, -1)]
        

    def allocate(self, size, mID):
        """
        :type size: int
        :type mID: int
        :rtype: int
        """
        for i in range(self.n):
            if self.locationSumArr[i] >= size:
                for j in range(size):
                    self.memory[i+j] = mID
                    self.locationSumArr[i+j] = 0
                return i
        return -1

    def free(self, mID):
        """
        :type mID: int
        :rtype: int
        """
        count = 0
        for i in range(self.n-1, -1, -1):
            if self.memory[i] == mID:
                self.memory[i] = 0
                count += 1
                if i == self.n-1:
                    self.locationSumArr[i] = 1    
                else:
                    self.locationSumArr[i] = self.locationSumArr[i+1] + 1
                check = i-1
                while self.memory[check] == 0 and check >=0:
                    self.locationSumArr[check] = self.locationSumArr[check+1] + 1
                    check -= 1
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
