# Soluzione ottimizzata per LeetCode 2561 - Rearranging Fruits
# Con commenti dettagliati su ogni passaggio

from typing import List
from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        Algoritmo ottimizzato:
        1. Conta le occorrenze di ogni frutto in entrambe le basket.
        2. Verifica che per ogni frutto la somma delle occorrenze sia pari (altrimenti impossibile).
        3. Calcola per ogni frutto quante unità sono "in eccesso" in basket1 e basket2 rispetto alla metà.
        4. Costruisci una lista di tutti i frutti da swappare (solo quelli in eccesso).
        5. Ordina la lista dei frutti da swappare per costo.
        6. Per ogni swap, il costo minimo è min(valore frutto, 2 * valore minimo globale).
        7. Somma i costi degli swap necessari.
        """
        # 1. Conta le occorrenze
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total = count1 + count2

        # 2. Verifica che la somma delle occorrenze sia pari per ogni frutto
        for fruit in total:
            if total[fruit] % 2 != 0:
                return -1

        # 3. Calcola le differenze (quante unità sono in eccesso in basket1 e basket2)
        excess1 = []  # Frutti da togliere da basket1
        excess2 = []  # Frutti da togliere da basket2
        for fruit in total:
            target = total[fruit] // 2
            if count1[fruit] > target:
                excess1 += [fruit] * (count1[fruit] - target)
            if count2[fruit] > target:
                excess2 += [fruit] * (count2[fruit] - target)

        # 4. Se non ci sono frutti da swappare, le basket sono già uguali
        if not excess1 and not excess2:
            return 0

        # 5. Ordina le due liste: una crescente, una decrescente
        excess1.sort()
        excess2.sort(reverse=True)

        # 6. Trova il valore minimo globale tra tutti i frutti
        min_fruit = min(total.keys())

        # 7. Calcola il costo minimo per ogni swap
        cost = 0
        for a, b in zip(excess1, excess2):
            # Per ogni swap, il costo minimo è min(a, b, 2 * min_fruit)
            cost += min(a, b, 2 * min_fruit)
        return cost

# Esempi di test
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    basket1 = [4,2,2,2]
    basket2 = [1,4,1,2]
    print("Output Example 1:", sol.minCost(basket1, basket2))  # Expected: 1

    # Example 2
    basket1 = [2,3,4,1]
    basket2 = [3,2,5,1]
    print("Output Example 2:", sol.minCost(basket1, basket2))  # Expected: -1

    # Custom Test
    basket1 = [84,80,43,8,80,88,43,14,100,88]
    basket2 = [32,32,42,68,68,100,42,84,14,8]
    print("Output Custom Test:", sol.minCost(basket1, basket2))  # Expected: 48

    # Large Test
    basket1 = list(range(1, 103))
    basket2 = list(range(100001, 100103))
    print("Output Large Test:", sol.minCost(basket1, basket2))  # Expected: -1
