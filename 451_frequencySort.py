from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        data = Counter(s)
        print("data", data)
        out = ''

ss = Solution()
s = "raaeaedere"
print(ss.frequencySort(s))