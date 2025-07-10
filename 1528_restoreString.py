from typing import List


class Solution:
	def restoreString(self, s: str, indices: List[int]) -> str:
		map = dict(zip(indices, list(s)))
		li = []
		for number in range(len(s)):
			li.append(map[number])
		return "".join(li)


ss = Solution()
s = "codeleet"
indices = [4, 5, 6, 7, 0, 1, 2, 3]
print(ss.restoreString(s, indices))
