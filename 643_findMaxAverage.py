from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ranges = len(nums)-k+1
        result = -1000
        for i in range(ranges):
            cur = sum(nums[0+i:k+i])/k
            result = max(cur, result)
        return result
    

ss = Solution()
nums = [5]
k = 1
print(ss.findMaxAverage(nums, k))