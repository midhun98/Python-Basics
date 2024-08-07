from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        length = int(len(candyType)/2)
        candies = int(len(set(candyType)))
        if length == candies or candies > length:
            return length
        else:
            return candies

ss = Solution()
candyType = [1,1,2,3]
print(ss.distributeCandies(candyType))