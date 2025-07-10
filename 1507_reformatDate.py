class Solution:
	def reformatDate(self, date: str) -> str:
		months = {
			"Jan": "01",
			"Feb": "02",
			"Mar": "03",
			"Apr": "04",
			"May": "05",
			"Jun": "06",
			"Jul": "07",
			"Aug": "08",
			"Sep": "09",
			"Oct": "10",
			"Nov": "11",
			"Dec": "12",
		}
		d, m, y = date.split(" ")
		dat = ""
		for i in d:
			if i.isnumeric():
				dat += i
		if len(dat) == 1:
			dat = "0" + dat
		return str(y + "-" + months[m] + "-" + dat)


ss = Solution()
date = "6th Jun 1933"
# out = "2052-10-20"
print(ss.reformatDate(date))
