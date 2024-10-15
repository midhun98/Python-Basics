class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            stack.append(char)
            if char == "]":
                if len(stack) > 1 and stack[-2] == "[":
                    stack.pop()
                    stack.pop()
            elif char == ")":
                if len(stack) > 1 and stack[-2] == "(":
                    stack.pop()
                    stack.pop()
            elif char == "}":
                if len(stack) > 1 and stack[-2] == "{":
                    stack.pop()
                    stack.pop()

        return len(stack) == 0


ss = Solution()
s = "()[]{}}"
print(ss.isValid(s))
