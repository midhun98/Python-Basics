class Solution:
	def maxScore(self, s: str) -> int:
		zero = 0
		ones = s.count("1")
		# print(zero, ones)
		res = 0
		for i in range(len(s) - 1):
			if s[i] == "0":
				zero += 1
			else:
				ones -= 1
			res = max(res, zero + ones)
		return res


ss = Solution()
s = "011101"
print(ss.maxScore(s))
