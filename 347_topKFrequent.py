from collections import Counter


class Solution:
	def topKFrequent(self, nums: list[int], k: int) -> list[int]:
		res = []
		count = 0
		data = Counter(nums).most_common()
		print("Data", data)
		for item in data:
			res.append(item[0])
			count += 1
			if count == k:
				break
		return res

nums = [1, 1, 1, 2, 2, 3]
k = 2
ss = Solution()
print(ss.topKFrequent(nums, k))
