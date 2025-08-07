# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        count = 0
        n = len(prices)
        while count < n:
            min_index = prices.index(min(prices))
            next = min_index + 1
            if next >= len(prices):
                this_profit = 0
                prices.remove(prices[min_index])
                count += 1
                continue
            max_index_on_remaining = prices.index(max(prices[next:]))
            this_profit = prices[max_index_on_remaining] - prices[min_index]
            profit = max(this_profit,profit)
            prices.pop(min_index)
            count += 1
        return profit