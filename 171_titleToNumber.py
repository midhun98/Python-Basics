class Solution:
	def titleToNumber(self, columnTitle: str) -> int:
		out = 0
		columnTitle = columnTitle[::-1]
		for index, letter in enumerate(columnTitle):
			num = ord(letter) - 64
			out += 26**index * num
		return out


ss = Solution()
columnTitle = "BB"
print(ss.titleToNumber(columnTitle))
