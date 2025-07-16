from collections import Counter


class Solution:
	def firstUniqChar(self, s: str) -> int:
		data = Counter(s)
		for key, value in data.items():
			if value == 1:
				return key
		return -1


ss = Solution()
s = "geeksforgeeks"
print(ss.nonRepeatingChar(s))
