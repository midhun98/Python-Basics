class Solution:
    def romanToInt(self, s: str) -> int:
        data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman = s
        li = [i for i in roman]
        num_li = []
        for num in li:
            num_li.append(data[num])

        counter = 1
        out = 0
        for num in num_li:
            try:
                if num > num_li[counter] or num == num_li[counter]:
                    out += num
                elif num < num_li[counter]:
                    out -= num
                counter += 1
            except:
                out += num_li[-1]
        return out
    
class Solution2:
    def romanToInt(self, s: str) -> int:
        data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        n = len(s)

        for i in range(n):
            if i < n - 1 and data[s[i]] < data[s[i + 1]]:
                total -= data[s[i]]
            else:
                total += data[s[i]]

        return total
