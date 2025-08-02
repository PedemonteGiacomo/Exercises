from typing import List
# Soluzione ottimizzata per LeetCode 560: Subarray Sum Equals K
# Usa una mappa dei prefissi per trovare tutte le sottosequenze che sommano a k in O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Calcola il numero di sottosequenze continue che sommano a k.
        Algoritmo:
        - Mantieni una mappa dei prefissi (somma cumulata -> occorrenze)
        - Per ogni elemento, aggiorna la somma cumulata
        - Se (somma cumulata - k) è già stata vista, aggiungi il suo conteggio
        """
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}  # La somma 0 esiste una volta (caso base)
        for num in nums:
            prefix_sum += num
            # Se esiste una sottosequenza che termina qui e somma a k
            count += prefix_map.get(prefix_sum - k, 0)
            # Aggiorna la mappa dei prefissi
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        return count

# Esempi di test
if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1,1,1], 2))  # Output: 2
    print(s.subarraySum([1,2,3], 3))  # Output: 2
    print(s.subarraySum([-1,-1,1], 0))  # Output: 1
    print(s.subarraySum([1,-1,0], 0))  # Output: 3
    # Test con input grande (dovrebbe essere veloce)
    import random
    nums = [random.randint(-1000, 1000) for _ in range(100000)]
    print(s.subarraySum(nums, 0))
