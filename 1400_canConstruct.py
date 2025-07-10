from collections import Counter


class Solution:
	def canConstruct(self, s: str, k: int) -> bool:
		if len(s) < k:
			return False
		count = Counter(s)
		odd_count = 0
		for number in count.values():
			if number % 2 == 1:
				odd_count += 1

		return odd_count <= k
