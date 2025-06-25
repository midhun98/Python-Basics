class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


ss = Solution()
s = "Hello, my name is John"
print(ss.countSegments(s))
