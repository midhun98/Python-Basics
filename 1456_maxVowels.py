class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        v_count = 0
        for i in range(k):
            if s[i] in vowels:
                v_count += 1
        if v_count == k:
            return k
        res = v_count

        for i in range(k, len(s)):
            if s[i] in vowels:
                v_count += 1
            if s[i - k] in vowels:
                v_count -= 1
            res = max(res, v_count)
            if res == k:
                return k
        return res


ss = Solution()
s = "abciiidef"
k = 3
print(ss.maxVowels(s, k))
