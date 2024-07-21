from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom = Counter(ransomNote)
        count_magazine = Counter(magazine)
        common = dict(count_ransom&count_magazine)
        return common == count_ransom

ss = Solution()
ransomNote = 'aa'
magazine = 'ab'
ss.canConstruct(ransomNote, magazine)