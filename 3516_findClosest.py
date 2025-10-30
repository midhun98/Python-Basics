class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        per1 = abs(z - x)
        per2 = abs(z - y)
        if per1 < per2:
            return 1
        elif per2 < per1:
            return 2
        else:
            return 0




x = 2
y = 7
z = 4

ss = Solution()
print(ss.findClosest(x,y,z))
