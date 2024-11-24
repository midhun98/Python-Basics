from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        max_sum = 0

        for i in range(length - k + 1):
            current_sum = 0
            unique_elements = set()
            valid = True

            for j in range(i, i + k):
                if nums[j] in unique_elements:
                    valid = False
                    break
                unique_elements.add(nums[j])
                current_sum += nums[j]

            if valid:
                max_sum = max(max_sum, current_sum)

        return max_sum


class Solution2:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        from collections import Counter

        max_sum = 0
        current_sum = 0
        count = Counter()

        for i, num in enumerate(nums):
            current_sum += num
            count[num] += 1

            if i >= k:
                left_num = nums[i - k]
                current_sum -= left_num
                count[left_num] -= 1
                if count[left_num] == 0:
                    del count[left_num]

            if len(count) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum


ss = Solution()
nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(ss.maximumSubarraySum(nums, k))
