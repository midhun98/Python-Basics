class Solution:
	def decompressRLElist(self, nums: list[int]) -> list[int]:
		res = []
		for i in range(1, len(nums), 2):
			res += [nums[i]] * nums[i - 1]
		return res


ss = Solution()
nums = [1, 2, 3, 4]
print(ss.decompressRLElist(nums))
