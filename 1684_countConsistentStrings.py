from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            word = set(word)
            if word.issubset(allowed):
                count += 1
        return count


class Solution2:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            word = set(word)
            flag = True
            for letter in word:
                if letter not in allowed:
                    flag = False
                    break
            count += flag
        return count


ss = Solution()
allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
print(ss.countConsistentStrings(allowed, words))
