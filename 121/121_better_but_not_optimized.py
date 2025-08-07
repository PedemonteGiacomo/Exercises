class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        n = len(prices)
        for i in range(n):
            min_price = prices[i]
            # Cerca il massimo solo nella parte successiva
            if i < n - 1:
                max_price = max(prices[i+1:])
                profit = max(profit, max_price - min_price)
        return profit