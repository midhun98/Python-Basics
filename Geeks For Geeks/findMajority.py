from collections import Counter


class Solution:
	def findMajority(self, arr):
		data = dict(Counter(arr))
		out = []
		n = len(arr)

		for key, value in data.items():
			if value > n // 3:
				out.append(key)

		return out


ss = Solution()
arr = [4, 5, 6, 4, 5, 6, 4, 5, 6]
print(ss.findMajority(arr))
