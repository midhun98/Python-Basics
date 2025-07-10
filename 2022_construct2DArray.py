from typing import List


class Solution:
	def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
		if m * n != len(original):
			return []

		out = []
		pointer = 0
		for _ in range(m):
			li = []
			for _ in range(n):
				li.append(original[pointer])
				pointer += 1
			out.append(li)
		return out


ss = Solution()
original = [1, 2, 3]
m = 1
n = 3
print(ss.construct2DArray(original, m, n))
