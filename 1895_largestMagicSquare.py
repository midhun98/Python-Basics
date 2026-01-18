class Solution:

    def calculate_sum(self, grid: list[list[int]]):
        rows = []
        cols = []
        diags = []
        for row in grid:
            rows.append(row)
        
        n = len(grid)
        for col in range(n):
            column = []
            for row in range(n):
                column.append(grid[row][col])
            cols.append(column)

        main_diag = []
        anti_diag = []
        for i in range(n):
            main_diag.append(grid[i][i])
            anti_diag.append(grid[i][n - 1 - i])

        diags.append(main_diag)
        diags.append(anti_diag)

        rows_sum = set([sum(li) for li in rows])
        cols_sum = set([sum(li) for li in cols])
        diags_sum = set([sum(li) for li in diags])
        
        if len(rows_sum) == 1 and len(cols_sum) == 1 and len(diags_sum) == 1:
            return rows_sum == cols_sum == diags_sum
        return False

    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for k in range(min(rows, cols), 1, -1):
            for r in range(rows - k + 1):
                for c in range(cols - k + 1):
                    subgrid = [row[c:c+k] for row in grid[r:r+k]]
                    if self.calculate_sum(subgrid):
                        return k
        return 1

ss = Solution()
grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
print(ss.largestMagicSquare(grid))