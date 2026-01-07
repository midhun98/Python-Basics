class Solution:
	def finalString(self, s: str) -> str:
		out = ""
		for char in s:
			if char != "i":
				out += char
			else:
				out = out[::-1]
		return out


ss = Solution()
s = "poiinter"
print(ss.finalString(s))
