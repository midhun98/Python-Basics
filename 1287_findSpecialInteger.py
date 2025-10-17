from typing import List
from collections import Counter


class Solution:
	def findSpecialInteger(self, arr: List[int]) -> int:
		data = Counter(arr)
		out = 0
		res = 0
		for key, value in data.items():
			if value > out:
				out = value
				res = key
		return res


ss = Solution()
arr = [1, 2, 2, 6, 6, 6, 6, 7, 10]
print(ss.findSpecialInteger(arr))
