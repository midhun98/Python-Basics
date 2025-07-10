from typing import List


class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		n = len(matrix)
		for i in range(n):
			for j in range(i + 1, n):  # for j in range(i, n):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		for row in matrix:
			row.reverse()


ss = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(ss.rotate(matrix))
