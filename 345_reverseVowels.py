class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        vowels_s = []
        for letter in s:
            if letter in vowels:
                vowels_s.append(letter)

        vowels_s = vowels_s[::-1]

        counter = 0
        for index, letter in enumerate(s):
            if letter in vowels:
                s[index] = vowels_s[counter]
                counter += 1
        return "".join(s)


ss = Solution()
s = "leetcode"
print(ss.reverseVowels(s))
