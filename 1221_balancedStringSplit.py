class Solution:
	def balancedStringSplit(self, s: str) -> int:
		res = 0
		count = 0
		for letter in s:
			if letter == "R":
				count += 1
			if letter == "L":
				count -= 1
			if count == 0:
				res += 1
		return res


ss = Solution()
s = "RLRRLLRLRL"
print(ss.balancedStringSplit(s))
