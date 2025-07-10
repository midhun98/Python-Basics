from collections import Counter
from typing import List


class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		count = Counter(nums)
		result = []
		for number in count:
			result.extend([number] * min(count[number], 2))
		nums[:] = result
		return len(result)


ss = Solution()
nums = [1, 1, 1, 2, 2, 3]
print(ss.removeDuplicates(nums))
