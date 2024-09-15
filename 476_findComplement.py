class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        inv_binary = [str(int(i)^1) for i in str(binary)]
        out = ''.join(inv_binary)
        return int(out, 2)

ss = Solution()
num = 5
print(ss.findComplement(num))