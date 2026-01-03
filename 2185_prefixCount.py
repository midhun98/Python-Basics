class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        res = 0
        for word in words:
            if word.startswith(pref):
                res += 1
        return res


ss = Solution()
words = ["pay","attention","practice","attend"]
pref = "at"

print(ss.prefixCount(words, pref))