from typing import List


class Solution:
	def findRelativeRanks(self, score: List[int]) -> List[str]:
		scores = sorted(score, reverse=True)
		out = {}
		counter = 1
		for i in scores:
			if counter == 1:
				out[i] = "Gold Medal"
			if counter == 2:
				out[i] = "Silver Medal"
			if counter == 3:
				out[i] = "Bronze Medal"
			if counter > 3:
				out[i] = str(counter)
			counter += 1
		res = []
		for i in score:
			res.append(out[i])
		return res


ss = Solution()
score = [10, 3, 8, 9, 4]
print(ss.findRelativeRanks(score))
