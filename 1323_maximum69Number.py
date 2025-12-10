class Solution:
	def maximum69Number(self, num: int) -> int:
		li = [num + 3000, num + 300, num + 30, num + 3, num]
		highest = 0
		for item in li:
			maximum = max(item, highest)
			if len(str(maximum)) < len(str(num)) + 1:
				highest = max(highest, maximum)
		return highest


ss = Solution()
num = 9669
print(ss.maximum69Number(num))
