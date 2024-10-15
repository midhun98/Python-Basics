from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_dict = dict(Counter(text))

        count = 0
        try:
            while (
                text_dict["b"] >= 1
                and text_dict["a"] >= 1
                and text_dict["l"] >= 2
                and text_dict["o"] >= 2
                and text_dict["n"] >= 1
            ):
                text_dict["b"] -= 1
                text_dict["a"] -= 1
                text_dict["l"] -= 2
                text_dict["o"] -= 2
                text_dict["n"] -= 1
                count += 1
            return count
        except:
            return 0


ss = Solution()
text = "nlaebolko"
print(ss.maxNumberOfBalloons(text))
