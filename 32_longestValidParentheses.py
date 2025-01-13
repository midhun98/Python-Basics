class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        count = 0
        for char in s:
            stack.append(char)
            if len(stack)>1 and char == ')' and stack[-2] == "(":
                stack.pop()
                stack.pop()
                count += 2
        return count

ss = Solution()
s = "()(()"
print(ss.longestValidParentheses(s))