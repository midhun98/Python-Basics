from typing import List


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		data = {}
		for index, num in enumerate(nums):
			diff = target - num
			if diff in data:
				return [index, data[diff]]

			data[num] = index


ss = Solution()
nums = [2, 7, 11, 15]
target = 9
print(ss.twoSum(nums, target))
