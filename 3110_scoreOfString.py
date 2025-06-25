class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_values = [ord(c) for c in s]
        out = []
        for i in range(len(ascii_values) - 1):
            out.append(abs(ascii_values[i] - ascii_values[i + 1]))
        return sum(out)


ss = Solution()
s = "hello"
print(ss.scoreOfString(s))
