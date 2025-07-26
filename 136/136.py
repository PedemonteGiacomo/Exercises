class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # soluzione semplice, hash map in cui tengo il conto di quante volte sto incontrando un particolare numero
        dictionary_ = {}

        for i in range(len(nums)):
            dictionary_[nums[i]] = dictionary_.get(nums[i], 0) + 1

        # restituisco il valore associato alla key che ha valore 1
        for key in dictionary_:
            if dictionary_[key] == 1:
                return key

# Time complexity: O(n)
# Space complexity: O(n)
        
# questa soluzione è O(n) in tempo e O(n) in spazio
# perché sto iterando su tutti gli elementi una volta e sto usando un dizionario per
# memorizzare il conteggio delle occorrenze di ciascun numero.
# Se avessi usato un set, avrei potuto ottenere una soluzione O(n) in spazio, ma non sarebbe stata
# possibile ottenere il conteggio delle occorrenze.
# Tuttavia, questa soluzione non è la più efficiente in termini di spazio.
# Potrei ottimizzare ulteriormente utilizzando l'operazione XOR.

# https://leetcode.com/problems/single-number/description/