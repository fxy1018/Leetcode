'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

'''

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        self.shuffledArray = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.shuffledArray = list(self.array)
        return(self.array)
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        remain = list(self.shuffledArray)
        
        for i in range(len(self.shuffledArray)):
            selectIndex = random.randrange(len(remain))
            self.shuffledArray[i] = remain.pop(selectIndex)
        
        return(self.shuffledArray)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
