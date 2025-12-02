class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = ""
        for char in s:
            if char == '(':
                if stack:
                    res += char
                stack.append('(')
            else:
                stack.pop()
                if stack:
                    res += char
        return res

ss = Solution()
s = "((()))()"
print(ss.removeOuterParentheses(s))