from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        out = []
        li = sorted(set(arr))
        ranks = {}
        for index, number in enumerate(li):
            ranks[number] = index + 1
        for number in arr:
            out.append(ranks[number])
        return out


ss = Solution()
arr = [40, 10, 20, 30]
print(ss.arrayRankTransform(arr))
