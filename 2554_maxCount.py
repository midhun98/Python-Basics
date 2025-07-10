from typing import List


class Solution:
	def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
		banned = set(banned)
		li = set()
		for num in range(1, n + 1):
			if num not in banned:
				li.add(num)

		count = 0
		total = 0
		li = sorted(li)

		for num in li:
			if total + num > maxSum:
				break
			total += num
			count += 1
		return count


ss = Solution()
banned = [1, 6, 5]
n = 5
maxSum = 6
print(ss.maxCount(banned, n, maxSum))
