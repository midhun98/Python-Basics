from typing import List


class Solution:
	def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
		out = []
		for num in nums1:
			n = nums2.index(num)
			li = nums2[n + 1 :]
			found = False
			for nu in li:
				if nu > num:
					out.append(nu)
					found = True
					break
			if not found:
				out.append(-1)
		return out


ss = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(ss.nextGreaterElement(nums1, nums2))
