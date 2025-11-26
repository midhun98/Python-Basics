class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        str1 = ''
        str2 = ''
        for st in word1:
            str1 += st
        for st in word2:
            str2 += st

        return str1 == str2


ss = Solution()
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(ss.arrayStringsAreEqual(word1, word2))
