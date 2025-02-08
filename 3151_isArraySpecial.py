from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if (nums[i]%2 == 0) == (nums[i+1]%2==0):
                return False
        return True


ss = Solution()
nums = [4,3,1,6]
print(ss.isArraySpecial(nums))