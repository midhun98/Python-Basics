from typing import List

'''
i like to imagine it like an obstacle,
if a maximum sum subarray exists in a circular formation, i.e. the left and right ends of the array,
then the obstacle in the middle will be the minimum sum subarray, so taking the total – global min,
we get the circular portion which is the globalmax 
'''


class Solution:
	def maxSubarraySumCircular(self, nums: List[int]) -> int:
		curr_sum = 0
		max_sum = nums[0]
		curr_min = 0
		min_sum = nums[0]
		total = 0
		for n in nums:
			curr_sum = max(curr_sum + n, n)
			max_sum = max(max_sum, curr_sum)
			curr_min = min(curr_min + n, n)
			min_sum = min(min_sum, curr_min)
			total += n
		return max(total - min_sum, max_sum) if max_sum > 0 else max_sum


ss = Solution()
nums = [5, -3, 5]
print(ss.maxSubarraySumCircular(nums))
