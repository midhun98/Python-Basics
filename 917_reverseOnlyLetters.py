class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = ''
        non_alpha = {}
        for index, letter in enumerate(s):
            if letter.isalpha():
                letters += letter
            else:
                non_alpha[index] = letter 
        letters = letters[::-1]

        
        res = []
        letter_index = 0
        list_non_alpha_keys = list(non_alpha.keys())

        for i in range(len(s)):
            if i in list_non_alpha_keys:
                res.append(non_alpha[i])
            else:
                res.append(letters[letter_index])
                letter_index += 1
        res = ''.join(res)
        return res

ss= Solution()
s = "ab-cd"
print(ss.reverseOnlyLetters(s))