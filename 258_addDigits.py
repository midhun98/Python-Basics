class Solution:
	def addDigits(self, num: int) -> int:
		num = str(num)
		out = 0
		if len(num) == 1:
			return int(num)
		else:
			while len(num) != 1:
				num = str(num)
				for i in num:
					out += int(i)
				num = str(out)
				out = 0
				if len(num) == 1:
					return int(num)
