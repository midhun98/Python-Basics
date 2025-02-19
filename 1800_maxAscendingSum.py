from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur = nums[0]
        out = cur

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += nums[i]
            else:
                cur = nums[i]
            out = max(cur, out)
        return out


ss = Solution()
nums = [10,20,30,5,10,50]
print(ss.maxAscendingSum(nums))
