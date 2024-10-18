class Solution:
    def intToRoman(self, num: int) -> str:
        data = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "IX": 9,
            "X": 10,
            "V": 5,
            "IV": 4,
            "I": 1,
        }
        out = []
        for index, value in data.items():
            while num > 0:
                if num >= value:
                    out.append(index)
                    num -= value
                else:
                    break
        return "".join(out)


ss = Solution()
num = 59
print(ss.intToRoman(num))
