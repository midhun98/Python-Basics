from typing import List
from collections import defaultdict


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        data = {}
        n = len((grid))
        for li in grid:
            for num in li:
                data[num] += 1

        repeated = -1
        missing = -1

        for i in range(1, n * n + 1):
            if i not in data:
                missing = i
            elif data[i] == 2:
                repeated = i
        return [repeated, missing]


ss = Solution()
grid = [[1, 3], [2, 2]]
print(ss.findMissingAndRepeatedValues(grid))
