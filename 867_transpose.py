from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        len_rows = len(matrix)
        len_cols = len(matrix[0])
        transponse = []
        for i in range(len_cols):
            li = []
            for j in range(len_rows):
                li.append(matrix[j][i])
            transponse.append(li)
        return transponse


ss = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(ss.transpose(matrix))
