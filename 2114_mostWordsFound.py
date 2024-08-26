from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        out = 0
        for sentence in sentences:
            len_sentence = len(sentence.split())
            if len_sentence > out:
                out = len_sentence
        return out


ss = Solution()
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(ss.mostWordsFound(sentences))