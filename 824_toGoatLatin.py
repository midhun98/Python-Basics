class Solution:
	def toGoatLatin(self, sentence: str) -> str:
		vowels = ["a", "e", "i", "o", "u"]
		sentence = sentence.split()
		out = ""
		count = 1
		for word in sentence:
			if word[0].lower() in vowels:
				out += word + "ma" + "a" * count + " "
			else:
				letter = word[0]
				word = word[1:]
				out += word + letter + "ma" + "a" * count + " "
			count += 1
		return out.strip()


ss = Solution()
sentence = "zzGPuClvxA XYbNe"
print(ss.toGoatLatin(sentence))
