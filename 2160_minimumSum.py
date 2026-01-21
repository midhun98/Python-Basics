class Solution:
	def minimumSum(self, num: int) -> int:
		num = sorted([i for i in str(num)])
		return int(num[0] + num[2]) + int(num[1] + num[3])


ss = Solution()
num = 2932
print(ss.minimumSum(num))
