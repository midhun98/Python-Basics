from typing import List
from collections import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)


ss = Solution()
target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
print(ss.canBeEqual(target, arr))
