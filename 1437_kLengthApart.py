from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        for number in nums:
            if number == 0:
                count += 1
            if number == 1:
                if count < k:
                    return False
                count = 0
        return True


ss = Solution()
nums = [1, 0, 0, 0, 1, 0, 0, 1]
k = 2
print(ss.kLengthApart(nums, k))
