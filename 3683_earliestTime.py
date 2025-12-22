class Solution:
    def earliestTime(self, tasks: list[list[int]]) -> int:
        out = []
        for li in tasks:
            out.append(sum(li))
        return min(out)


ss = Solution()
tasks = [[1,6],[2,3]]
print(ss.earliestTime(tasks))
        