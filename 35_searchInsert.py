from typing import List


class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		if target in nums:
			return nums.index(target)
		else:
			nums.append(target)
			nums.sort()
			return nums.index(target)


nums = [1, 3, 5, 6]
target = 2
ss = Solution()
print(ss.searchInsert(nums, target))
