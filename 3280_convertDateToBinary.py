class Solution:
	def convertDateToBinary(self, date: str) -> str:
		binary = ""
		date = date.split("-")
		for d in date:
			binary += format(int(d), "b") + "-"
		return binary.rstrip("-")


date = "2080-02-29"

ss = Solution()
print(ss.convertDateToBinary(date))
