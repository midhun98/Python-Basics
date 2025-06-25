from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        if count > 1:
            return False
        return True


ss = Solution()
# nums = [3,4,5,1,2]
nums = [2, 1, 3, 4]
print(ss.check(nums))
