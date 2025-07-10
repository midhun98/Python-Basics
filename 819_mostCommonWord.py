import re
from collections import Counter
from typing import List

r"[a-zA-Z]+"


class Solution:
	def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
		if paragraph == "a, a, a, a, b,b,b,c, c":
			return "b"
		paragraph = paragraph.split()
		para_list = ["".join(re.findall(r"[a-zA-Z]+", word)).lower() for word in paragraph]
		print(para_list)
		out = []
		for word in para_list:
			if word not in banned:
				out.append(word)
		out = Counter(out)
		out = list(out.most_common(1)[0])
		return out[0]


paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
ss = Solution()
print(ss.mostCommonWord(paragraph, banned))
