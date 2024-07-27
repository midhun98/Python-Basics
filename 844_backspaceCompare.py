class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for letter in s:
            if letter != '#':
                stack_s.append(letter)
            if '#' in letter and len(stack_s)!=0:
                stack_s.pop()
        for letter in t:
            if letter != '#':
                stack_t.append(letter)
            if '#' in letter and len(stack_t)!=0:
                stack_t.pop()

        return stack_s == stack_t

ss = Solution()
s = "a##c"
t = "#a#c"
print(ss.backspaceCompare(s, t))