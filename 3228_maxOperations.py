class Solution:
    def maxOperations(self, s: str) -> int:
        s = [int(i) for i in list(s)]
        pref = []
        ones_count = 0
        for num in s:
            if num == 1:
                ones_count += 1
                pref.append(ones_count)
            else:
                pref.append(ones_count)

        li = []
        for i in range(len(s)):
            if s[i] == 0:
                li.append(pref[i])

        return sum(set(li))


ss = Solution()
s = "10011010"
print(ss.maxOperations(s))
