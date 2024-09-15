class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split(" ")
        for index, word in enumerate(sentence):
            word = word[0 : len(searchWord)]
            if searchWord in word:
                return index + 1
        return -1


ss = Solution()
sentence = "this problem is an easy problem"
searchWord = "pro"
print(ss.isPrefixOfWord(sentence, searchWord))
