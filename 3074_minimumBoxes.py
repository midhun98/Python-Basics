class Solution:
	def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
		capacity = sorted(capacity, reverse=True)
		total = sum(apple)
		res = 1
		sums = 0
		for i in capacity:
			sums += i
			if sums < total:
				res += 1
		return res


ss = Solution()

apple = [5, 5, 5]
capacity = [2, 4, 2, 7]
ss.minimumBoxes(apple, capacity)
