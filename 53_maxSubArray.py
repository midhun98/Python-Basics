from typing import List


class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		max_sum = nums[0]
		curr_max = nums[0]

		for i in range(1, len(nums)):
			curr_max = max(nums[i], curr_max+nums[i])
			max_sum = max(curr_max, max_sum)

		return max_sum


ss = Solution()
nums = [-1, -1, -3, 4, -1, 2, 1, -5, 4]
print(ss.maxSubArray(nums))
