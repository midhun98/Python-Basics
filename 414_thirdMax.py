from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        nums = nums[0:3]
        if len(nums) == 3:
            return nums[2]
        return nums[0]


ss = Solution()
nums = [3, 2, 1]
print(ss.thirdMax(nums))
