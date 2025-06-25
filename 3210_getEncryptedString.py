class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        out = ""
        counter = 0
        n = len(s)
        for _ in s:
            num = (counter + k) % n
            out += s[num]
            counter += 1
        return out


ss = Solution()
s = "dart"
k = 3
print(ss.getEncryptedString(s, k))
