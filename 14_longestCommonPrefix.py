from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        longest = ""
        length = len(strs)

        for index, letter in enumerate(first):
            word = first[0 : index + 1]
            counter = 0
            for st in strs:
                if st.startswith(word):
                    counter += 1
            if counter == length:
                longest += letter
            else:
                break
        return longest


strs = ["flower", "flow", "flight"]
ss = Solution()
print(ss.longestCommonPrefix(strs))
