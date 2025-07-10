class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		if s == "":
			return 0
		li = []
		length = len(s)
		for left in range(length):
			sub = ""
			for r in range(left, length):
				if s[r] in sub:
					break
				sub += s[r]
			li.append(sub)
		li = [len(i) for i in li]
		return max(li)


ss = Solution()
s = "pwwkew"
print(ss.lengthOfLongestSubstring(s))
