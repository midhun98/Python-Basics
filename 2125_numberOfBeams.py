from typing import List


class Solution:
	def numberOfBeams(self, bank: List[str]) -> int:
		out = []
		for b in bank:
			if "1" in b:
				out.append(b)

		res = []
		for b in out:
			res.append(b.count("1"))

		result = 0
		n = len(res) - 1
		for i in range(n):
			result += res[i] * res[i + 1]
		return result


ss = Solution()
bank = ["011001", "000000", "010100", "001000"]
print(ss.numberOfBeams(bank))
