from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out = []
        for index, word in enumerate(words):
            if x in word:
                out.append(index)
        return out


ss = Solution()
words = ["abc", "bcd", "aaaa", "cbc"]
print(ss.findWordsContaining(words))
