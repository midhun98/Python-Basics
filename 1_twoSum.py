from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for index, number in enumerate(nums):
            num = target - number
            if num in data:
                return [data[num], index]
            data[number] = index

ss = Solution()
nums = [2,7,11,15]
target = 9
print(ss.twoSum(nums, target))