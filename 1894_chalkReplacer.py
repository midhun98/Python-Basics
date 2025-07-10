from typing import List


class Solution:
	def chalkReplacer(self, chalk: List[int], k: int) -> int:
		total_chalk = sum(chalk)
		remaining_chalk = k % total_chalk
		for index, number in enumerate(chalk):
			remaining_chalk -= number
			if remaining_chalk < 0:
				return index


ss = Solution()
chalk = [3, 4, 1, 2]
k = 25
print(ss.chalkReplacer(chalk, k))
