from collections import Counter


class Solution:
	def areAnagrams(self, s1, s2):
		if len(s1) != len(s2):
			return False
		count1 = Counter(s1)
		count2 = Counter(s2)
		return count1 == count2


ss = Solution()
s1 = "geeks"
s2 = "kseeg"
