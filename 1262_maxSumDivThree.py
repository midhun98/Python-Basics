class Solution:
	def maxSumDivThree(self, nums: list[int]) -> int:
		total = sum(nums)

		if total % 3 == 0:
			return total

		rem1 = []
		rem2 = []

		for x in nums:
			if x % 3 == 1:
				rem1.append(x)
			elif x % 3 == 2:
				rem2.append(x)

		rem1.sort()
		rem2.sort()

		out = []
		if total % 3 == 1:
			if rem1:
				out.append(total - rem1[0])
			if len(rem2) >= 2:
				out.append(total - rem2[0] - rem2[1])

		if total % 3 == 2:
			if rem2:
				out.append(total - rem2[0])
			if len(rem1) >= 2:
				out.append(total - rem1[0] - rem1[1])
		return max(out)


ss = Solution()

nums = [3,6,5,1,8]
print(ss.maxSumDivThree(nums))
