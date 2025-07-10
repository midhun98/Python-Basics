class Solution:
	def countDigits(self, num: int) -> int:
		numbers = [int(i) for i in str(num)]
		count = 0
		for n in numbers:
			if num % n == 0:
				count += 1
		return count


ss = Solution()
num = 1248
print(ss.countDigits(num))
