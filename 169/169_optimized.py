# https://leetcode.com/problems/majority-element/
# Soluzione ottimizzata O(n) spazio O(1) con Boyer-Moore Voting Algorithm
# Commenti passo-passo

class Solution(object):
    def majorityElement(self, nums: list[int]) -> int:
        """
        Trova l'elemento che appare più di n/2 volte.
        Algoritmo:
        - Mantieni un candidato e un contatore
        - Se il contatore è 0, scegli il candidato corrente
        - Se il numero è uguale al candidato, incrementa il contatore
        - Altrimenti decrementa il contatore
        """
        candidate = None  # Candidato attuale per la maggioranza
        count = 0         # Contatore per il candidato
        # Scorri tutti gli elementi dell'array
        for num in nums:
            if count == 0:
                # Se il contatore è zero, scegli il nuovo candidato
                candidate = num
                count = 1
            elif num == candidate:
                # Se il numero è uguale al candidato, incrementa il contatore
                count += 1
            else:
                # Se il numero è diverso, "elimina" una coppia candidato/altro
                count -= 1
            # (In pratica, ogni volta che trovi un diverso, bilanci il conteggio)
        # Alla fine, il candidato rimasto è quello che ha "resistito" a tutte le eliminazioni
        # Questo funziona solo se esiste davvero una maggioranza (> n/2)
        return candidate

# Esempi di test
if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3,2,3]))  # Output: 3
    print(s.majorityElement([2,2,1,1,1,2,2]))  # Output: 2
