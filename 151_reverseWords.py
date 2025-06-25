class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        li.reverse()
        return " ".join(li)


s = "  hello world  "
ss = Solution()
print(ss.reverseWords(s))
