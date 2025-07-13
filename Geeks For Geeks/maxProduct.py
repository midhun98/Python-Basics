from typing import List


class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		curr_max = curr_min = max_prod = nums[0]
		n = len(nums)
		for i in range(1, n):
			a = nums[i]
			curr_min, curr_max = min(a, a * curr_max, a * curr_min), max(a, a * curr_max, a * curr_min)
			max_prod = max(curr_max, max_prod)
		return max_prod


ss = Solution()
nums = [2, -5, 3, -4]
print(ss.maxProduct(nums))
