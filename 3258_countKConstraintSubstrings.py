class Solution:
	def countKConstraintSubstrings(self, s: str, k: int) -> int:
		n = len(s)
		count = 0
		for i in range(n):
			ones = 0
			zeros = 0
			for j in range(i, n):
				if s[j] == "0":
					zeros += 1
				else:
					ones += 1
				if zeros <= k or ones <= k:
					count += 1
				else:
					break
		return count


ss = Solution()
s = "10101"
k = 1
print(ss.countKConstraintSubstrings(s, k))
