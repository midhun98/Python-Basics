class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


ss = Solution()
n = 1
print(ss.canWinNim(n))
