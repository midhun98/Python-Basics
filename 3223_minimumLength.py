from collections import Counter


class Solution:
	def minimumLength(self, s: str) -> int:
		count = Counter(s)
		out = 0
		for num in count.values():
			if num % 2 == 0:
				out += 2
			else:
				out += 1
		return out


ss = Solution()
s = "abaacbcbb"
print(ss.minimumLength(s))
