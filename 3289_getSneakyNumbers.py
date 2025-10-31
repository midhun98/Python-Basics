from collections import Counter


class Solution:
	def getSneakyNumbers(self, nums: list[int]) -> list[int]:
		data = Counter(nums)
		res = []
		for key, value in data.items():
			if value == 2:
				res.append(key)
		return res


ss = Solution()
nums = [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]
print(ss.getSneakyNumbers(nums))
