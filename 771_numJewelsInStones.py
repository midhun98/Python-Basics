from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_count = dict(Counter(stones))
        counter = 0
        for letter in jewels:
            if letter in stones_count:
                counter += stones_count[letter]
        return counter
    
ss = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(ss.numJewelsInStones(jewels, stones))