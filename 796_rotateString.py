class Solution:
	def rotateString(self, s: str, goal: str) -> bool:
		if len(s) != len(goal):
			return False
		concat = s + s
		if goal in concat:
			return True
		return False


ss = Solution()
s = "abcde"
goal = "abced"
print(ss.rotateString(s, goal))
