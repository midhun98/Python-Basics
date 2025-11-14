# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/solutions/7344834/solution-by-la_castille-vdqt
class Solution:
    def maxOperations(self, s: str) -> int:
        arr = [int(i) for i in s]
        pref = []
        ones_count = 0
        for num in arr:
            if num == 1:
                ones_count += 1
                pref.append(ones_count)
            else:
                pref.append(ones_count)
        li = []
        for i in range(len(s)):
            if arr[i] == 0:
                li.append(pref[i])

        return sum(set(li))


ss = Solution()
s = "10011010"
print(ss.maxOperations(s))
