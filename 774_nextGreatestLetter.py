from typing import List


class Solution:
    @staticmethod
    def binary_search(arr: List[str], target: str) -> int:
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = self.binary_search(letters, target)
        print(index)
        if index == len(letters):
            return letters[0]
        return letters[index]


letters = ["c", "f", "j"]
target = "c"
ss = Solution()
print(ss.nextGreatestLetter(letters, target))
