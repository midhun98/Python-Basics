class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
                if len(factors) == k:
                    return i
        return -1


ss = Solution()
n = 4   
k = 4
print(ss.kthFactor(n, k))