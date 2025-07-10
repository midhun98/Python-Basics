from typing import List


class Solution:
	def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
		small = min(nums)
		large = max(nums)
		if len(nums) == 1 and small == 1:
			return []
		if small == large and small == 1:
			return [small + 1]
		if small == large and small != 1:
			return [small - 1]
		li = [i for i in range(1, len(nums) + 1)]
		missing = list(set(li) - set(nums))
		return missing


ss = Solution()
nums = [1]
print(ss.findDisappearedNumbers(nums))
