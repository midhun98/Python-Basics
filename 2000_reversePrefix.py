class Solution:
	def reversePrefix(self, word: str, ch: str) -> str:
		word = list(word)
		split_index = None
		for index, char in enumerate(word):
			if char == ch:
				split_index = index
				break
		if split_index:
			word = word[: split_index + 1][::-1] + word[split_index + 1 :]

		word = "".join(word)
		return word


ss = Solution()
word = "abcdefd"
ch = "d"
print(ss.reversePrefix(word, ch))
