class Solution:
	def areAlmostEqual(self, s1: str, s2: str) -> bool:
		if s1 == s2:
			return True
		if len(s1) != len(s2):
			return False

		diff = []
		for i in range(len(s1)):
			if s1[i] != s2[i]:
				diff.append(i)

		if len(diff) == 2:
			i, j = diff
			print(i, j)
			if s1[i] == s2[j] and s1[j] == s2[i]:
				return True

		return False


ss = Solution()
s1 = "bank"
s2 = "kanb"
print(ss.areAlmostEqual(s1, s2))
