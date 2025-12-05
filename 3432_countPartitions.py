class Solution:
	def countPartitions(self, nums: list[int]) -> int:
		res = 0
		total = sum(nums)
		left = 0
		right = 0
		for i in range(len(nums)-1):
			left += nums[i]
			right = total - left
			if (left - right) % 2 == 0:
				res += 1

		return res


ss = Solution()
nums = [10, 10, 3, 7, 6]
print(ss.countPartitions(nums))
