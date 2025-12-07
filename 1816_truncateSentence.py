class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])


ss = Solution()
s = "Hello how are you Contestant"
k = 4
print(ss.truncateSentence(s, k))
