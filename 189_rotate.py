from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            num = nums.pop()
            nums.insert(0, num)


ss = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(ss.rotate(nums, k))
