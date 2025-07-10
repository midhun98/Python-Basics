from typing import List


class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		num3 = nums1 + nums2
		num3.sort()
		len_num3 = len(num3)
		if len_num3 % 2 == 0:
			a = len_num3 // 2
			b = a - 1
			return (num3[a] + num3[b]) / 2
		else:
			a = len_num3 // 2
			return num3[a]


ss = Solution()
nums1 = []
nums2 = [1]
print(ss.findMedianSortedArrays(nums1, nums2))
