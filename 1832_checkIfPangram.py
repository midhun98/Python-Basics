class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26       



ss = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(ss.checkIfPangram(sentence))