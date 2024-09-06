from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        out = []
        for x,y in zip(nums, index):
            out.insert(y, x)
        return out

ss = Solution()
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(ss.createTargetArray(nums, index))