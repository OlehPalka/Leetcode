class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        for price in range(len(prices) - 1):
            if prices[price] - prices[price + 1] < 0:
                max_profit -= prices[price] - prices[price + 1]
        return max_profit
