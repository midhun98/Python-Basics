class Solution:
	def makeFancyString(self, s: str) -> str:
		stack = []
		for letter in s:
			stack.append(letter)
			if len(stack) > 2:
				if stack[-1] == stack[-2] == stack[-3]:
					stack.pop()
		return "".join(stack)


ss = Solution()
s = "aaabaaaa"
print(ss.makeFancyString(s))
