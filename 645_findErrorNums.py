from typing import List


class Solution:
	def findErrorNums(self, nums: List[int]) -> List[int]:
		nums = sorted(nums)
		for num in range(len(nums) - 1):
			if nums[num] == nums[num + 1]:
				out = nums[num]
				break

		n = len(nums)
		complete_set = set(range(1, n + 1))
		nums_set = set(nums)
		missing_num = list(complete_set - nums_set)[0]
		return [out, missing_num]


ss = Solution()
nums = [1, 1]
print(ss.findErrorNums(nums))
