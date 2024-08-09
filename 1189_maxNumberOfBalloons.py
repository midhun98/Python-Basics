from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_dict = dict(Counter(text))
        ball_dict = dict(Counter('balloon'))    
        print(text_dict)
        print(ball_dict)


ss = Solution()
text = "nlaebolko"
print(ss.maxNumberOfBalloons(text))