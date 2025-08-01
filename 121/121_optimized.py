# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Inizializza il prezzo minimo visto finora a infinito
        min_price = float('inf')
        # Inizializza il massimo profitto a zero
        max_profit = 0
        # Scorri tutti i prezzi uno per uno
        for price in prices:
            # Se il prezzo attuale è più basso del minimo visto finora, aggiorna min_price
            if price < min_price:
                min_price = price
            # Se vendendo al prezzo attuale si ottiene un profitto maggiore di quello massimo visto finora, aggiorna max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
        # Restituisce il massimo profitto ottenuto
        return max_profit
