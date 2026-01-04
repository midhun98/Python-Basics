class Solution:
	def minimumAverage(self, nums: list[int]) -> float:
		averages = []
		nums = sorted(nums)
		n = len(nums) // 2
		averages.append((nums[0] + nums[-1]) / 2)
		for _ in range(n):
			nums = nums[1:-1]
			try:
				averages.append((nums[0] + nums[-1]) / 2)
			except:
				pass

		return min(averages)


ss = Solution()
nums = [1, 9, 8, 3, 10, 5]
print(ss.minimumAverage(nums))
