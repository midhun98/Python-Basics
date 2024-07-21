from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            if num == 0:
                current_count = 0
        return max_count

ss = Solution()
nums = [1,1,0,1,1,1]
print(ss.findMaxConsecutiveOnes(nums))