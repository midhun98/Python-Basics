class Solution:
	def countSymmetricIntegers(self, low: int, high: int) -> int:
		res = 0

		for i in range(low, high + 1):
			i = str(i)
			if len(i) % 2 == 0:
				if len(i) == 2:
					left = i[0]
					right = i[1]

					if left == right:
						res += 1
				if len(i) == 4:
					left = i[:2]
					left_sum = sum([int(i) for i in left])
					right = i[2:]
					right_sum = sum([int(i) for i in right])
					if left_sum == right_sum:
						res += 1
		return res


ss = Solution()
low = 1200
high = 1230
print(ss.countSymmetricIntegers(low, high))
