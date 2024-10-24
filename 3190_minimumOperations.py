from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        out = 0
        for num in nums:
            if num % 3 == 0:
                continue
            else:
                if (num - 1) % 3 == 0 or (num + 1) % 3 == 0:
                    out += 1
        return out


ss = Solution()
nums = [1, 2, 3, 4]
print(ss.minimumOperations(nums))
