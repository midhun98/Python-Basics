class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] != diff:
                return False
        return True


ss = Solution()
arr = [-13,-17,-8,-10,-20,2,3,-19,2,-18,-5,7,-12,18,-17,12,-1]

print(ss.canMakeArithmeticProgression(arr))
