from typing import List


class Solution:
	def canBeIncreasing(self, nums: List[int]) -> bool:
		for index in range(len(nums)):
			nums_copy = nums[:index] + nums[index + 1 :]
			if nums_copy == sorted(list(set(nums_copy))):
				return True
		return False


class Solution2:
	def canBeIncreasing(self, nums: List[int]) -> bool:
		violation = 0

		for i in range(1, len(nums)):
			if nums[i] <= nums[i - 1]:
				violation += 1
				if violation > 1:
					return False
				if i > 1 and nums[i] <= nums[i - 2] and nums[i + 1] <= nums[i - 1]:
					return False
		return True


ss = Solution()
nums = [2, 3, 1, 2]
print(ss.canBeIncreasing(nums))
