from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        element_sum =sum(nums)
        digit_sum = 0
        for num in nums:
            num = str(num)
            for n in num:
                digit_sum += int(n)
        return element_sum - digit_sum

ss = Solution()
nums = [1,2,3,4]
print(ss.differenceOfSum(nums))