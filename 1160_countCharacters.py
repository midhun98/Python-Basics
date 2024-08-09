from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_dict = dict(Counter(chars))
        out = 0
        for word in words:
            w = dict(Counter(word))
            can_form_word = True
            for key, _ in w.items():
                if w[key] > char_dict.get(key, 0):
                    can_form_word = False
                    break
            if can_form_word:
                out += len(word)
        return out


ss = Solution()
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(ss.countCharacters(words, chars))