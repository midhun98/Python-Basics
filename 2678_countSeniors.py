from typing import List


class Solution:
	def countSeniors(self, details: List[str]) -> int:
		count = 0
		for data in details:
			age = int(data[11:13])
			if age > 60:
				count += 1
		return count


ss = Solution()
details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
print(ss.countSeniors(details))
