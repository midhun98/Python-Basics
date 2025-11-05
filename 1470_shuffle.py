class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        out = []
        r = n
        length = len(nums) // 2
        for i in range(length):
            out.append(nums[i])
            out.append(nums[r])
            r += 1
        return out


ss = Solution()
nums = [2,5,1,3,4,7]
n = 3
print(ss.shuffle(nums, n))
