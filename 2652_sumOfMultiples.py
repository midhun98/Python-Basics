class Solution:
	def sumOfMultiples(self, n: int) -> int:
		out = 0
		for i in range(1, n + 1):
			if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
				print(i)
				out += i
		return out


ss = Solution()
n = 7
print(ss.sumOfMultiples(n))
