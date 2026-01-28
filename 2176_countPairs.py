class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        out = 0
        n = len(nums)
        for i in range(n - 1):
            for j in range(i+1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    out += 1
        return out


ss = Solution()
nums = [3,1,2,2,2,1,3]
k = 2