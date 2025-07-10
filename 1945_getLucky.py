class Solution:
	def getLucky(self, s: str, k: int) -> int:
		out = "".join(str(ord(c) - 96) for c in s)
		for _ in range(k):
			final = sum(int(i) for i in out)
			out = str(final)
		return final


class Solution2:
	def getLucky(self, s: str, k: int) -> int:
		out = "".join(str(ord(c) - 96) for c in s)
		for _ in range(k):
			final = str(sum(int(i) for i in out))
		return final


ss = Solution()
s = "leetcode"
k = 2
print(ss.getLucky(s, k))
