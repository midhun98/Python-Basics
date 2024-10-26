class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        li = [i for i in range(1, n + 1)]
        divisble = 0
        non_divisble = 0
        for num in li:
            if num % m == 0:
                divisble += num
            else:
                non_divisble += num
        return non_divisble - divisble


ss = Solution()
n = 10
m = 3
print(ss.differenceOfSums(n, m))
