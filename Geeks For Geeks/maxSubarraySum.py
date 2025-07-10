class Solution:
	def maxSubarraySum(self, arr):
		curr_sum = arr[0]
		max_sum = arr[0]

		for i in range(1, len(arr)):
			curr_sum = max(arr[i], arr[i] + curr_sum)
			max_sum = max(curr_sum, max_sum)
		return max_sum


ss = Solution()

arr = [4, -1, 3, 2]
print(ss.maxSubarraySum(arr))
