from typing import List


class Solution:
	def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
		data = {}

		for id, val in nums1:
			data[id] = val

		for id, val in nums2:
			if id in data:
				data[id] += val
			else:
				data[id] = val

		res = []
		for num in sorted(data):
			res.append([num, data[num]])
		return res


ss = Solution()
nums1 = [[1, 2], [2, 3], [4, 5]]
nums2 = [[1, 4], [3, 2], [4, 1]]
print(ss.mergeArrays(nums1, nums2))
