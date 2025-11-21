class Solution:
	def countPalindromicSubsequence(self, s: str) -> int:
		res = 0
		uniques = set(s)
		for char in uniques:
			left = s.find(char)
			right = s.rfind(char)
			if left < right:
				res += len(set(s[left + 1 : right]))
		return res


ss = Solution()
s = "aabca"
print(ss.countPalindromicSubsequence(s))
