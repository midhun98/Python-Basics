from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        def custom_sort(n):
            return(count[n], -n)
        
        nums.sort(key=custom_sort)
        return nums
    
ss = Solution()
nums = [1,1,2,2,2,3]
print(ss.frequencySort(nums))