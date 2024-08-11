from typing import List
from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        data = Counter(nums)
        print(data.most_common(1)[0][0])
        for key, value in data.items():
            if value >= 2:
                return key

ss = Solution()
nums = [1,2,3,3]
print(ss.repeatedNTimes(nums))