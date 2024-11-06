class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""

        out = ""
        length = len(word) - 1
        count = 1

        for i in range(length):
            if word[i] == word[i + 1]:
                count += 1
            else:
                out += str(count) + word[i]
                count = 1

            if count == 10:
                count -= 1
                out += str(count)
                out += word[i]
                count = 1
        out += str(count) + word[-1]
        return out


ss = Solution()
word = "aaayy"
print(ss.compressedString(word))
