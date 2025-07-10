from typing import List


class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		nums1[0 : m + n] = sorted(nums1[0:m] + nums2[0:n])


ss = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(ss.merge(nums1, m, nums2, n))
