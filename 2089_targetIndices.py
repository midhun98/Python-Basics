from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        out = []
        nums = sorted(nums)
        print(nums)
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                out.append(mid)
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1


ss = Solution()
nums = [1, 2, 5, 2, 3]
target = 2
print(ss.targetIndices(nums, target))
