class Solution:
    def isBalanced(self, num: str) -> bool:
        odd = 0
        even = 0 

        n = len(num)
        for j in range(0, n, 2):
            odd += int(num[j])
        for j in range(1, n, 2):
            even += int(num[j])
        return odd == even

ss = Solution()
num = "24123"

print(ss.isBalanced(num))