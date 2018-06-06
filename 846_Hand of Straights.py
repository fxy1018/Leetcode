'''
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
 

Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length

'''
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        length = len(hand)
        if length % W != 0:
            return(False)
        
        cardHash = {}
        for c in hand:
            cardHash[c] = cardHash.get(c,0) + 1
        
        for i in range(length//W):
            start = min(cardHash.keys())
            cardHash[start] = cardHash[start]-1
            if cardHash[start] == 0:
                del(cardHash[start])
            for j in range(1, W):
                if start + j in cardHash:
                    cardHash[start+j] = cardHash[start+j]-1
                    if cardHash[start+j] == 0:
                        del(cardHash[start+j])
                else:
                    return(False)
        return(True)
