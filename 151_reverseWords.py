class Solution:
    def reverseWords(self, s: str) -> str:
        li=s.split().reverse()
        li.reverse()
        return " ".join(li)

s =  "  hello world  "
ss = Solution()
print(ss.reverseWords(s))