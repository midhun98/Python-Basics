class Solution:
	def reversePrefix(self, s: str, k: int) -> str:
		s1 = s[:k][::-1]
		s2 = s[k:]
		return s1 + s2


ss = Solution()
s = "xyz"
k = 3

print(ss.reversePrefix(s, k))
