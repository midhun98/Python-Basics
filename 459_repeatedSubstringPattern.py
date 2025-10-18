from collections import Counter


class Solution:
	def repeatedSubstringPattern(self, s: str) -> bool:
		data = (s + s)[1:-1]
		return s in data


ss = Solution()
s = "abcabcabcabc"
print(ss.repeatedSubstringPattern(s))
