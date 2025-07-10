class Solution:
	def maximumProfit(self, prices) -> int:
		max_profit = 0
		buy_price = prices[0]

		for price in prices:
			profit = price - buy_price
			if profit > max_profit:
				max_profit = profit

			if price < buy_price:
				buy_price = price

		return max_profit


ss = Solution()
prices = [100, 180, 260, 310, 40, 535, 695]
print(ss.maximumProfit(prices))
