class Solution:
	def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
		out = []
		sorted_nums = sorted(nums)
		smaller_count = {}
		for i, num in enumerate(sorted_nums):
			if num not in smaller_count:
				smaller_count[num] = i

		for num in nums:
			out.append(smaller_count[num])

		return out


ss = Solution()
nums = [7,7,7,7]
print(ss.smallerNumbersThanCurrent(nums))
