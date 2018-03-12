'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.


'''

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        l1 = len(list1)
        l2 = len(list2)
    
        
        likeOne = [[l1+l2, ""]]
        list1Hash = {}
        list2Hash = {}
        for i in range(l1):
            list1Hash[list1[i]] = i
            
        for j in range(l2):
            rest = list2[j]
            if rest in list1Hash:
                if j + list1Hash[rest] < likeOne[0][0]:
                    likeOne = [[j + list1Hash[rest], rest]]
                elif j + list1Hash[rest] == likeOne[0][0]:
                    likeOne.append([j + list1Hash[rest], rest])
        return([x[1] for x in likeOne])
                
            
