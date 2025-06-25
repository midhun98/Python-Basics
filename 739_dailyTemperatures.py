from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = []
        length = len(temperatures)
        for index, temp in enumerate(temperatures):
            found = False
            for i in range(index + 1, length):
                if temperatures[i] > temp:
                    out.append(i - index)
                    found = True
                    break
            if not found:
                out.append(0)

        return out


ss = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(ss.dailyTemperatures(temperatures))
