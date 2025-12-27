class Solution:
	def countKDifference(self, nums: list[int], k: int) -> int:
		res = 0
		n = len(nums)
		for i in range(n):
			for j in range(i + 1, n):
				if abs(nums[i] - nums[j]) == k:
					res += 1
		return res


ss = Solution()
nums = [1, 2, 2, 1]
k = 1
print(ss.countKDifference(nums, k))
