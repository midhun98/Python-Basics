class Solution:
	def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
		count = 0
		words = text.split(" ")
		for word in words:
			has_broken = False
			for letter in brokenLetters:
				if letter in word:
					has_broken = True
					break
    
			if not has_broken:
				count += 1
		return count


class Solution2:
	def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
		count = 0
		words = text.split(" ")
		for word in words:
			if not any(letter in word for letter in brokenLetters):
				count += 1
		return count


ss = Solution()
text = "leet code"
brokenLetters = "lt"
print(ss.canBeTypedWords(text, brokenLetters))
