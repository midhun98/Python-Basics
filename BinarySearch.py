from typing import List

class Solution:
    def binarysearch(self, numbers: List[int], find: int) -> int:
        low = 0
        high = len(numbers) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_number = numbers[mid]
            if mid_number == find:
                return mid
            elif mid_number < find:
                low = mid + 1
            else:
                high = mid - 1
        return -1


ss = Solution()
numbers = [0,1,2,3,4,5,6,7,8,9]
find = 6
print(ss.binarysearch(numbers, find))