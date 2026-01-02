from collections import Counter
from typing import List


class Solution:
	def repeatedNTimes(self, nums: List[int]) -> int:
		data = Counter(nums)
		print(data.most_common(1)[0][0])
		for key, value in data.items():
			if value >= 2:
				return key


ss = Solution()
nums = [2,1,2,5,3,2]
print(ss.repeatedNTimes(nums))
