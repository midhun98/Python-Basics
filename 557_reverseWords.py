class Solution:
	def reverseWords(self, s: str) -> str:
		out = ""
		s = s.split(" ")
		for word in s:
			out += word[::-1] + " "
		return out.strip()


ss = Solution()
s = "Let's take LeetCode contest"
print(ss.reverseWords(s))
