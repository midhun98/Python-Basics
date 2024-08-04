from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        out = []
        for number in candies:
            if number + extraCandies >= highest:
                out.append(True)
            else:
                out.append(False)
        return out
ss = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(ss.kidsWithCandies(candies, extraCandies))