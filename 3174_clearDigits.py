class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for letter in s:
            if letter.isalpha():
                stack.append(letter)
            if letter.isnumeric():
                stack.pop()
        return ''.join(stack)

ss = Solution()
s = "cb34"
print(ss.clearDigits(s))