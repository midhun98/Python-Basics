class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        len_s = len(s)
        count = 0
        for i in s:
            if i == letter:
                count += 1
        percentage = (count/len_s)*100
        return int(percentage)

ss = Solution()
s = "foobar"
letter = "o"
print(ss.percentageLetter(s, letter))