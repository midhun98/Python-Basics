class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        li = []
        sentence = sentence.split(" ")
        length = len(sentence) - 1
        for i in range(length):
            li.append(sentence[i][-1] == sentence[i + 1][0]
        if len(sentence) > 1:
            li.append(sentence[0][0] == sentence[-1][-1])
        if len(sentence) == 1:
            return sentence[0][0] == sentence[-1][-1]
        if False in li:
            return False
        return True


ss = Solution()
sentence = "leetcode"

print(ss.isCircularSentence(sentence))
