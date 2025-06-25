from typing import List
from collections import Counter


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        map = Counter(nums)
        for key, value in map.items():
            if value > 1:
                return key


ss = Solution()
nums = [1, 3, 4, 2, 2]
print(ss.findDuplicate(nums))
