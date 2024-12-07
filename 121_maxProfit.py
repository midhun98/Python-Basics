from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minmum_price = prices[0]

        for price in prices:
            if price < minmum_price:
                minmum_price = price
            profit = price - minmum_price

            if profit > max_profit:
                max_profit = profit

        return max_profit


ss = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(ss.maxProfit(prices))
