from typing import List


class Solution:
	def largestAltitude(self, gain: List[int]) -> int:
		start = 0
		res = 0
		for i in gain:
			start += i
			res = max(start, res)

		return res


ss = Solution()
gain = [-4,-3,-2,-1,4,3,2]

print(ss.largestAltitude(gain))
