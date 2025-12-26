class Solution:
	def romanToInt(self, s: str) -> int:
		data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
		length = len(s)
		last = s[-1]
		out = 0
		for i in range(length - 1):
			if data[s[i + 1]] > data[s[i]]:
				out -= data[s[i]]
			else:
				out += data[s[i]]
		return out + data[last]


ss = Solution()
s = "III"
print(ss.romanToInt(s))
