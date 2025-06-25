from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] > nums[j] + nums[i]:
                    continue
                else:
                    nums[i], nums[j] = nums[j], nums[i]
        nums = "".join(nums)
        return str(int(nums))


ss = Solution()
nums = [3, 30, 34, 5, 9]
# nums = [10, 2]
print(ss.largestNumber(nums))
