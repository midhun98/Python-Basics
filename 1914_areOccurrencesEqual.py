from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count_dict = dict(Counter(s))
        if len(set(count_dict.values())) == 1:
            return True
        return False

ss = Solution()
s = "abacbc"
print(ss.areOccurrencesEqual(s))