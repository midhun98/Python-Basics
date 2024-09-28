from typing import List


class Solution:
    @staticmethod
    def left_search(nums, target):
        left = 0
        right = len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return result

    @staticmethod
    def right_search(nums, target):
        left = 0
        right = len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return result

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.left_search(nums, target)
        right = self.right_search(nums, target)
        return [left, right]


ss = Solution()
nums = []
target = 1
print(ss.searchRange(nums, target))
