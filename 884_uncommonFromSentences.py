from typing import List


class Solution:
	def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
		data = {}
		s3 = s1 + " " + s2
		s3 = s3.split()
		for word in s3:
			if word not in data:
				data[word] = 1
			else:
				data[word] += 1
		out = []
		for key, value in data.items():
			if value == 1:
				out.append(key)
		return out


ss = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(ss.uncommonFromSentences(s1, s2))
