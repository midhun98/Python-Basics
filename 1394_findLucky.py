from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        data = Counter(arr)
        out = []
        for key, value in data.items():
            if key == value:
                out.append(key)
        try:
            return max(out)
        except:
            return -1
arr = [2,2,2,3,3]

ss = Solution()
print(ss.findLucky(arr))