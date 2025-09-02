from typing import List


class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		# for _ in range(k):
		# 	num = nums.pop()
		# 	nums.insert(0, num)

		k = k % len(nums)
		arr = self.reverse(0, len(nums) - 1, nums)
		arr = self.reverse(0, k-1, arr)
		arr = self.reverse(k, len(nums)-1, arr)
		return arr

	def reverse(self, left, right, arr):
		while left < right:
			arr[left], arr[right] = arr[right], arr[left]
			left += 1
			right -= 1
		return arr


ss = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(ss.rotate(nums, k))
