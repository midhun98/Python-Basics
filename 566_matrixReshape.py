from typing import List


class Solution:
	def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
		numbers = []
		for li in mat:
			for num in li:
				numbers.append(num)

		if len(numbers) != r * c:
			return mat

		matrix = []
		counter = 0
		for i in range(r):
			row = []
			for j in range(c):
				row.append(numbers[counter])
				counter += 1
			matrix.append(row)
		return matrix


ss = Solution()
mat = [[1, 2], [3, 4]]
r = 4
c = 1
print(ss.matrixReshape(mat, r, c))
