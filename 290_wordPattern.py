class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        s = s.split()
        word_dict = {}

        counter = 0
        for word in s:
            if word not in word_dict:
                if pattern[counter] not in word_dict.values():
                    word_dict[word] = pattern[counter]
            counter += 1

        pattern_constructed = ""
        for word in s:
            try:
                pattern_constructed += word_dict[word]
            except:
                return False
        if pattern_constructed == pattern:
            return True


ss = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(ss.wordPattern(pattern, s))
