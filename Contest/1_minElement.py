from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        out = []
        for num in nums:
            num = str(num)
            sum = 0
            for i in num:
                sum += int(i)
            out.append(sum)
        return min(out)


ss = Solution()
nums = [999,19,199]
print(ss.minElement(nums))