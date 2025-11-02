class Solution:
	def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
		# 0: empty, 1: wall, 2: guard, 3: guarded
		grid = [[0] * n for _ in range(m)]
		for row, col in walls:
			grid[row][col] = 1

		for row, col in guards:
			grid[row][col] = 2

		for row, col in guards:
			# Right checking
			for c in range(col + 1, n):
				if grid[row][c] in [1, 2]:
					break
				if grid[row][c] == 0:
					grid[row][c] = 3

			# Left checking
			for c in range(col - 1, -1, -1):
				if grid[row][c] in [1, 2]:
					break
				if grid[row][c] == 0:
					grid[row][c] = 3

			# Down Checking
			for r in range(row + 1, m):
				if grid[r][col] in [1, 2]:
					break
				if grid[r][col] == 0:
					grid[r][col] = 3

			# Up checking
			for r in range(row - 1, -1, -1):
				if grid[r][col] in [1, 2]:
					break
				if grid[r][col] == 0:
					grid[r][col] = 3

		unguarded = 0
		for r in range(m):
			for c in range(n):
				if grid[r][c] == 0:
					unguarded += 1
		return unguarded


ss = Solution()
m = 4
n = 6
guards = [[0, 0], [1, 1], [2, 3]]
walls = [[0, 1], [2, 2], [1, 4]]

print(ss.countUnguarded(m, n, guards, walls))
