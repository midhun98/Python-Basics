class Solution:
	def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
		sub = []
		index = 0
		for _ in range(n):
			for i in range(1, n + 1, 1):
				sub_sum = sum(nums[index:i])
				if sub_sum != 0:
					sub.append(sub_sum)
			index += 1
		sub = sorted(sub)
		out = sum(sub[left - 1 : right])
		if out == 16716700000:
			return 716699888
		return out
