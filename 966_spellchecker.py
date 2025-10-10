from typing import List


class Solution2:
	def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
		def devowel(word: str) -> str:
			vowels = "aeiouAEIOU"
			result = ""
			for letter in word:
				if letter in vowels:
					result += "*"
				else:
					result += letter
			return result

		words_perfect = set(wordlist)
		words_cap = {}
		words_vow = {}

		for word in wordlist:
			word_lower = word.lower()
			words_cap.setdefault(word_lower, word)
			word_devow = devowel(word_lower)
			words_vow.setdefault(word_devow, word)

		out = []
		for query in queries:
			if query in words_perfect:
				out.append(query)
				continue

			query_lower = query.lower()
			if query_lower in words_cap:
				out.append(words_cap[query_lower])
				continue

			query_devow = devowel(query_lower)
			if query_devow in words_vow:
				out.append(words_vow[query_devow])
				continue
			out.append("")

		return out


ss = Solution2()
wordlist = ["KiTe", "kite", "hare", "Hare"]
query = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
print(ss.spellchecker(wordlist, query))
