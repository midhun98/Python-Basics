from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		low = 0
		high = len(nums) - 1
		while low <= high:
			mid = (low + high) // 2
			mid_number = nums[mid]
			if mid_number == target:
				return mid
			elif mid_number < target:
				low = mid + 1
			else:
				high = mid - 1
		return -1


ss = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 3
print(ss.search(nums, target))
