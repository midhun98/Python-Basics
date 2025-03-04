from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        p = []
        less = []
        great = []

        for num in nums:
            if num > pivot:
                great.append(num)   
            elif num < pivot:
                less.append(num)
            elif num == pivot:
                p.append(num)
        return less + p + great


ss = Solution()
nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
print(ss.pivotArray(nums, pivot))
