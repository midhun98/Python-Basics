from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        li = [format(i, "b") for i in range(n + 1)]
        for num in li:
            total = 0
            for i in num:
                total += int(i)
            out.append(total)
        return out


ss = Solution()
n = 5
print(ss.countBits(n))
