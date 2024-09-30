from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        length = len(mat)
        for _ in range(4):
            out = []
            for i in range(length):
                li = []
                for j in range(length):
                    li.append(mat[length - 1 - j][i])
                out.append(li)
            mat = out
            if out == target:
                return True
        return False


class Solution2:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        length = len(mat)
        for _ in range(4):
            out = []
            col = 0
            for _ in range(length):
                row = length - 1
                li = []
                for _ in range(length):
                    li.append(mat[row][col])
                    row -= 1
                col += 1
                out.append(li)
            mat = out
            if out == target:
                return True
        return False


ss = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
print(ss.findRotation(mat, target))
