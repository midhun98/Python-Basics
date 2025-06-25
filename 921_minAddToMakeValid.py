class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        close_count = 0
        for char in s:
            if char == "(":
                open_count += 1
            else:
                open_count -= 1
                if open_count < 0:
                    open_count = 0
                    close_count += 1
        return open_count + close_count


ss = Solution()
s = ")))"
print(ss.minAddToMakeValid(s))
