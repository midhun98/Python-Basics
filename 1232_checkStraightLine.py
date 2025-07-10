from typing import List


class Solution:
	def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
		if len(coordinates) == 2:
			return True

		x = []
		y = []
		for i in range(len(coordinates) - 1):
			li = coordinates[i]
			li2 = coordinates[i + 1]
			x1, y1 = abs(li[0]), abs(li[1])
			x2, y2 = abs(li2[0]), abs(li2[1])
			x.append(x2 - x1)
			y.append(y2 - y1)
		print(x)
		print(y)
		if x == y:
			return True
		return False


ss = Solution()
coordinates = [[0, 0], [0, 1], [0, -1]]
# coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]


print(ss.checkStraightLine(coordinates))
