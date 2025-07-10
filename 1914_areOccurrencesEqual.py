from collections import Counter


class Solution:
	def areOccurrencesEqual(self, s: str) -> bool:
		count_dict = Counter(s)
		if len(set(count_dict.values())) == 1:
			return True
		return False

		# count_dict = Counter(s)
		# return len(set(count_dict.values())) == 1


ss = Solution()
s = "abacbc"
print(ss.areOccurrencesEqual(s))
