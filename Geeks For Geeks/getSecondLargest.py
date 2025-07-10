class Solution:
	def getSecondLargest(self, arr):
		arr = sorted(list(set(arr)))
		if len(arr) == 1:
			return -1
		return arr[-2]


ss = Solution()
arr = [12, 35, 1, 10, 34, 1]
print(ss.getSecondLargest(arr))  # Output: 4
