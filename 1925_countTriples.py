class Solution:
	def countTriples(self, n: int) -> int:
		res = 0
		for a in range(1, n + 1):
			for b in range(1, n + 1):
				val = a * a + b * b
				c = int(val**0.5)

				if val == c * c:
					res += 1

		return res


ss = Solution()
n = 10

print(ss.countTriples(n))
