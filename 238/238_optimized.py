# Soluzione ottimizzata per LeetCode 238 - Product of Array Except Self
# Con commenti dettagliati su ogni passaggio

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Algoritmo ottimizzato:
        1. Calcola per ogni posizione il prodotto di tutti gli elementi a sinistra (prefix).
        2. Calcola per ogni posizione il prodotto di tutti gli elementi a destra (suffix).
        3. La risposta per ogni posizione è prefix[i] * suffix[i].
        4. Complessità O(n) e senza divisione.
        """
        n = len(nums)
        answer = [1] * n  # Inizializza la risposta con 1

        # 1. Calcola il prodotto dei prefissi (sinistra)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
            # answer[i] ora contiene il prodotto di tutti gli elementi a sinistra di i

        # 2. Calcola il prodotto dei suffissi (destra) e aggiorna la risposta
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            # answer[i] ora contiene il prodotto di tutti gli elementi a sinistra e destra di i

        return answer

# Esempi di test
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    print("Output Example 1:", sol.productExceptSelf(nums))  # Expected: [24,12,8,6]

    nums = [0,1,2,3]
    print("Output Example 2:", sol.productExceptSelf(nums))  # Expected: [6,0,0,0]

    nums = [2,3,4,5]
    print("Output Example 3:", sol.productExceptSelf(nums))  # Expected: [60,40,30,24]
