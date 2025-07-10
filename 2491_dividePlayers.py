from collections import Counter
from typing import List


class Solution:
	def dividePlayers(self, skill: List[int]) -> int:
		total = sum(skill)
		num_pairs = len(skill) // 2
		if total % num_pairs != 0:
			return -1
		target = total // num_pairs
		out = 0
		data = Counter(skill)

		for s in skill:
			if data[s] == 0:
				continue
			diff = target - s
			if data[diff] == 0:
				return -1
			out += s * diff
			data[s] -= 1
			data[diff] -= 1
		return out


ss = Solution()
skill = [1, 1, 1, 2, 3, 3, 3, 7, 7, 8, 8, 8, 9, 9]
print(ss.dividePlayers(skill))
