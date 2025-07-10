from typing import List


class Solution:
	def findClosestNumber(self, nums: List[int]) -> int:
		out = nums[0]
		for num in nums:
			if abs(num) < abs(out):
				out = num
				out = max(num, out)
		if out < 0 and abs(out) in nums:
			return abs(out)
		else:
			return out


ss = Solution()
nums = [2, -1, 1]

print(ss.findClosestNumber(nums))
