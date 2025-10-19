from collections import Counter


class Solution:
	def repeatedSubstringPattern(self, s: str) -> bool:
		data = (s + s)[1:-1]
		return s in data



class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rep = ''

        for i in range(len(s)//2):
            rep += s[i]
            if (len(s) % len(rep)) == 0:
                  if rep * (len(s) // len(rep)) == s:
                        return True
        return False

ss = Solution()
s = "abcabcabcabc"
print(ss.repeatedSubstringPattern(s))
