from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        counter_nums1 = Counter(nums1)
        counter_nums2 = Counter(nums2)
        intersection_counter = counter_nums1 & counter_nums2
        intersection_list = list(intersection_counter.elements())
        return intersection_list

ss = Solution()
nums1 = [1,2,2,1]
nums2 = [2]
print(ss.intersect(nums1, nums2))