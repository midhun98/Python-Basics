from typing import List


class Solution:
	def findMin(self, nums: List[int]) -> int:
		left, right = 0, len(nums) - 1
		while left < right:
			mid = (left + right) // 2
			if nums[mid] > nums[right]:
				left = mid + 1
			if nums[mid] < nums[right]:
				right = mid
		return nums[left]


ss = Solution()
# nums = [4, 5, 6, 7, 1, 2, 3]
nums = [11, 12, 13, 4, 5, 6, 7]
print(ss.findMin(nums))
