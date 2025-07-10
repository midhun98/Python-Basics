from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		left, right = 0, len(nums) - 1
		while left <= right:
			mid = (left + right) // 2
			if nums[mid] == target:
				return mid
			# Check if the left part is sorted
			if nums[left] <= nums[mid]:
				# Check if Target is in the left sorted part
				if nums[left] <= target < nums[mid]:
					right = mid - 1
				else:  # Target is in the right unsorted part
					left = mid + 1
			else:
				# Right part is sorted
				if nums[mid] < target <= nums[right]:
					left = mid + 1
				else:
					right = mid - 1
		return -1  # Target not found


ss = Solution()
nums = [4, 5, 6, 17, 0, 1, 2]
target = 1
print(ss.search(nums, target))
