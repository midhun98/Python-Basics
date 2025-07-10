from typing import List


class Solution:
	def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
		count = 0
		index = 0
		for _, _ in zip(startTime, endTime):
			for i in range(startTime[index], endTime[index] + 1):
				if i == queryTime:
					count += 1
			index += 1
		return count


class Solution2:
	def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
		count = 0
		for i in range(len(startTime)):
			if startTime[i] <= queryTime and endTime[i] >= queryTime:
				count += 1
		return count


ss = Solution2()
startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4
print(ss.busyStudent(startTime, endTime, queryTime))
