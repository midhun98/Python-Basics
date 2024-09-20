from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        return nums[-k]


ss = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(ss.findKthLargest(nums, k))