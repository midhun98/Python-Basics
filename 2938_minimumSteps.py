class Solution:
	def minimumSteps(self, s: str) -> int:
		steps = 0
		one_count = 0
		for char in s:
			if char == "1":
				one_count += 1
			if char == "0":
				steps += one_count
		return steps


ss = Solution()
s = "0110"
print(ss.minimumSteps(s))
