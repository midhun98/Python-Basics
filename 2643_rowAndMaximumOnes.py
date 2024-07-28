from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        highest = []
        for li in mat:
            highest.append(sum(li))
        return [highest.index(max(highest)), max(highest)]

ss = Solution()
mat = [[0,1],[1,0]]
print(ss.rowAndMaximumOnes(mat))