from typing import List


class Solution:
	def nextPermutation(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		i = len(nums) - 2
		while i >= 0 and nums[i] >= nums[i + 1]:
			print(nums[i])
			i -= 1


ss = Solution()
nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
print(ss.nextPermutation(nums))
