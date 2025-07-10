"""
Given a String str, reverse the string without reversing its individual words. Words are separated by dots.

Note: The last character has not been '.'.

Examples :

Input: str = i.like.this.program.very.much
Output: much.very.program.this.like.i
Explanation: After reversing the whole string(not individual words), the input string becomes much.very.program.this.like.i

"""


class Solution:
	def reverseWords(self, str):
		str = str.split(".")
		out = str[::-1]
		return ".".join(out)


ss = Solution()
sentence = "i.like.this.program.very.much"
print(ss.reverseWords(sentence))
