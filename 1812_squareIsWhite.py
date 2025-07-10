class Solution:
	def squareIsWhite(self, coordinates: str) -> bool:
		x, y = coordinates[0], coordinates[1]
		x = ord(x) - 96
		data = {"oddodd": False, "oddeven": True, "evenodd": True, "eveneven": False}
		out = ""
		if (int(x) % 2) == 0:
			out += "even"
		else:
			out += "odd"
		if (int(y) % 2) == 0:
			out += "even"
		else:
			out += "odd"
		return data[out]


ss = Solution()
coordinates = "a1"
print(ss.squareIsWhite(coordinates))
