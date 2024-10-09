class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2:
            return False
        data = {"}": "{", "]": "[", ")": "("}
        for char in s:
            if char in data:
                if stack and stack[-1] == data[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append(")")
            elif char == "[":
                stack.append("]")
            elif char == "{":
                stack.append("}")
            elif not stack or stack.pop() != char:
                return False
        return not stack


ss = Solution2()
s = "()[]{}}"
print(ss.isValid(s))
