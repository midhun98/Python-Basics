from collections import Counter
from typing import List


class Solution:
	def divideArray(self, nums: List[int]) -> bool:
		data = dict(Counter(nums))
		li = data.values()
		for num in li:
			if num % 2 != 0:
				return False
		return True


ss = Solution()
nums = [3, 2, 3, 2, 2, 2]
print(ss.divideArray(nums))
