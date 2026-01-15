class Solution:
	def sortSentence(self, s: str) -> str:
		s = s[::-1].split()
		s.sort()
		res = []
		for st in s:
			res.append(st[1:][::-1])

		return " ".join(res)


ss = Solution()
s = "is2 sentence4 This1 a3"
print(ss.sortSentence(s))
