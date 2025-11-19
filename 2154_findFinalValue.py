class Solution:
	def findFinalValue(self, nums: list[int], original: int) -> int:
		nums_set = set(nums)
		for _ in range(len(nums)):
			if original in nums_set:
				original *= 2
			else:
				return original
		return original


nums = [5, 3, 6, 1, 12]
original = 3
ss = Solution()
print(ss.findFinalValue(nums, original))
