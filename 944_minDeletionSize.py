class Solution:
	def minDeletionSize(self, strs: list[str]) -> int:
		rows = len(strs)
		cols = len(strs[0])
		res = 0

		for c in range(cols):
			for r in range(rows - 1):
				if strs[r][c] > strs[r + 1][c]:
					res += 1
					break
		return res


strs = ["zyx", "wvu", "tsr"]
ss = Solution()
print(ss.minDeletionSize(strs))
