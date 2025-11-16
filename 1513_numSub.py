class Solution:
	def numSub(self, s: str) -> int:
		res = 0
		cons = 0

		for num in s:
			if num == "1":
				cons += 1
				res += cons
			else:
				cons = 0
		return res % (10**9 + 7)


ss = Solution()
s = "0110111"
print(ss.numSub(s))
