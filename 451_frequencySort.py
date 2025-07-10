from collections import Counter


class Solution:
	def frequencySort(self, s: str) -> str:
		data = dict(Counter(s))
		values = sorted(set(data.values()), reverse=True)
		out = ""
		for num in values:
			for key, value in data.items():
				if num == value:
					out += key * num
		return out


class Solution(object):
	def frequencySort(self, s):
		out = ""
		data = Counter(s).most_common()
		for key, value in data:
			out += key * value
		return "".join(out)


ss = Solution()
s = "tree"
print(ss.frequencySort(s))
