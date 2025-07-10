class Solution1:
	def defangIPaddr(self, address: str) -> str:
		out = ""
		for char in address:
			if char == ".":
				out += "[.]"
			else:
				out += char
		return out


class Solution2:
	def defangIPaddr(self, address: str) -> str:
		return address.replace(".", "[.]")


ss = Solution1()
address = "1.1.1.1"
print(ss.defangIPaddr(address))
