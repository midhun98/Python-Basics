from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        count = 0
        g_p = 0
        s_p = 0
        while g_p < len(g):
            if g[g_p] <= s[s_p]:
                count += 1
                g_p += 1
                s_p += 1
            else:
                s_p += 1
        return count


ss = Solution()
g = [1, 2, 3]
s = [1, 1]
print(ss.findContentChildren(g, s))
