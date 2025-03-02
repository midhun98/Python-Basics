from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0
        return res


ss = Solution()
nums = [1, 1, 0, 1, 1, 1]
print(ss.findMaxConsecutiveOnes(nums))
