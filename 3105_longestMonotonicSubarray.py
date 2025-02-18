from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_len = 1
        dec_len = 1
        max_len = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                inc_len += 1
                dec_len = 1
            elif nums[i] > nums[i + 1]:
                dec_len += 1
                inc_len = 1
            else:
                inc_len = 1
                dec_len = 1
            max_len = max(max_len, inc_len, dec_len)
        return max_len


ss = Solution()
# nums = [1,2,10,1,3,1,2,10,4,3,2,1,0]
nums = [1, 4, 6, 5, 4]
print(ss.longestMonotonicSubarray(nums))
