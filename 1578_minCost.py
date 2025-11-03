class Solution:
	def minCost(self, colors: str, neededTime: list[int]) -> int:
		res = 0
		l = 0
		for r in range(1, len(colors)):
			if colors[l] == colors[r]:
				if neededTime[l] < neededTime[r]:
					res += neededTime[l]
					l = r
				else:
					res += neededTime[r]
			else:
				l = r
		return res


ss = Solution()
colors = "abaac"
neededTime = [1, 2, 3, 4, 5]
print(ss.minCost(colors, neededTime))
