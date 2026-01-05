class Solution:
	def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
		total = sum(int(i) for i in str(x))
		return total if x % total == 0 else -1


ss = Solution()
x = 18
print(ss.sumOfTheDigitsOfHarshadNumber(x))