class Solution:
	def findCenter(self, edges: list[list[int]]) -> int:
		l1 = edges[0]
		l2 = edges[1]
		if l1[0] == l2[0]:
			return l1[0]
		if l1[0] == l2[1]:
			return l1[0]
		if l1[1] == l2[1]:
			return l1[1]
		if l1[1] == l2[0]:
			return l1[1]


ss = Solution()
edges = [[1,2],[5,1],[1,3],[1,4]]
print(ss.findCenter(edges))
