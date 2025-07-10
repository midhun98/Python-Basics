from typing import List


class Solution:
	def maximumProduct(self, nums: List[int]) -> int:
		out = 1
		for num in nums:
			out *= num
		return out


ss = Solution()
nums = [-1, -2, -3]
print(ss.maximumProduct(nums))
