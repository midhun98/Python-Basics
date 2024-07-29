class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        total_len = len(word1) + len(word2) - 1
        res = ""
        pointer2 = 0
        pointer1 = 0
        for _ in range(total_len):
            try:
                res += word1[pointer1]
                pointer1 += 1
            except:
                pass
            try:
                res += word2[pointer2]
                pointer2 += 1
            except:
                pass
        return res


ss = Solution()
word1 = "abcd"
word2 = "pq"
print(ss.mergeAlternately(word1, word2))