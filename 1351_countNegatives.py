from typing import List


class Solution:
	def countNegatives(self, grid: List[List[int]]) -> int:
		out = 0
		for li in grid:
			out += sum(1 for i in li if i < 0)
		return out


ss = Solution()
grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

print(ss.countNegatives(grid))
