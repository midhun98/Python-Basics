from collections import Counter


class Solution:
	def maxFreqSum(self, s: str) -> int:
		data = dict(Counter(s))
		max_vowel = 0
		max_consonant = 0
		vowels = "aeiou"
		for key, value in data.items():
			if key in vowels:
				max_vowel = max(value, max_vowel)
			else:
				max_consonant = max(value, max_consonant)
		return max_vowel + max_consonant


ss = Solution()
s = "aeiaeia"
print(ss.maxFreqSum(s))
