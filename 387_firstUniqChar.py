class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for letter in s:
            if letter not in dic:
                dic[letter] = 1
            else:
                dic[letter] += 1

        for index, value in enumerate(s):
            if dic[value] == 1:
                return index
        return -1


ss = Solution()
s = "loveleetcode"
print(ss.firstUniqChar(s))
