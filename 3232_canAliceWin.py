from typing import List


class Solution:
	def canAliceWin(self, nums: List[int]) -> bool:
		singles = 0
		doubles = 0
		for num in nums:
			if len(str(num)) == 1:
				singles += num
			doubles += num
		if singles == doubles:
			return False
		return True


ss = Solution()
nums = [1, 2, 3, 4, 10]
print(ss.canAliceWin(nums))
