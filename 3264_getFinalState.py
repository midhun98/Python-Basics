class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        for i in range(k):
            smallest = min(nums)
            index_of_smallest = nums.index(smallest)
            nums[index_of_smallest] = nums[index_of_smallest] * multiplier
        return nums

ss = Solution()
nums = [2,1,3,5,6]
k = 5
multiplier = 2
print(ss.getFinalState(nums, k, multiplier))
