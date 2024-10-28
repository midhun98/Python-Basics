class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = 0
        zero_count = 0

        for num in s:
            if num == "0":
                zero_count += 1
            else:
                one_count += 1
        out = "1" * one_count + "0" * zero_count
        out = out[1:]
        return out + "1"


ss = Solution()
s = "0101"
print(ss.maximumOddBinaryNumber(s))
