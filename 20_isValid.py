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


ss = Solution()
s = "()[]{}"
print(ss.isValid(s))
