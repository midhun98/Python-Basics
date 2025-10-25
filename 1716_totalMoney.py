class Solution:
	def totalMoney(self, n: int) -> int:
		li = []
		num = 1
		out = 0
		for i in range(1, n + 1):
			li.append(num)
			out += num
			num += 1
			if i % 7 == 0:
				num = (i // 7) + 1
		return out


ss = Solution()
n = 4
print(ss.totalMoney(n))
