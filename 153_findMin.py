from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            if nums[low] <= nums[high]:
                return nums[low]
            mid = (low + high) // 2
            if nums[low] > nums[mid]:
                high = mid
            if nums[low] < nums[mid]:
                low = mid + 1


ss = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
print(ss.findMin(nums))
