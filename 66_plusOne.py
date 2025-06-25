from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num += str(i)
        num = str(int(num) + 1)
        out = []
        for i in num:
            out.append(int(i))
        return out


ss = Solution()
digits = [1, 2, 3]
print(ss.plusOne(digits))
