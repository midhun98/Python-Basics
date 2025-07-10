from typing import List


class Solution:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		if not matrix or not matrix[0]:
			return False

		rows = len(matrix)
		cols = len(matrix[0])

		left, right = 0, rows * cols - 1
		print("left + right", left + right)
		while left <= right:
			mid = (left + right) // 2
			# Calculate row and column based on mid index
			row = mid // cols
			col = mid % cols
			print("mid, cols: ", mid, cols)
			mid_value = matrix[row][col]
			print(row, col)
			if mid_value == target:
				return True
			elif mid_value < target:
				left = mid + 1
			elif mid_value > target:
				right = mid - 1

		return False


ss = Solution()
matrix = [[1, 3, 5, 7, 9], [10, 11, 16, 20, 21], [23, 30, 34, 60, 61]]
target = 16
print(ss.searchMatrix(matrix, target))
