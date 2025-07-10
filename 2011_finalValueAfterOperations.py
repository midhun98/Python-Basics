from typing import List


class Solution:
	def finalValueAfterOperations(self, operations: List[str]) -> int:
		out = 0
		for operation in operations:
			if "--" in operation:
				out -= 1
			else:
				out += 1
		return out


ss = Solution()
operations = ["--X", "X++", "X++"]
print(ss.finalValueAfterOperations(operations))
