from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		max_profit = 0
		buy_price = prices[0]

		for today_price in prices:
			if today_price < buy_price:
				buy_price = today_price

			profit = today_price - buy_price

			if profit > max_profit:
				max_profit = profit

		return max_profit


ss = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(ss.maxProfit(prices))
