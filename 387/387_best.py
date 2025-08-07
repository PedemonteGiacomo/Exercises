# Soluzione ottimale O(n) per il problema del primo carattere unico
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Primo passaggio: conta le occorrenze di ogni carattere
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        # Secondo passaggio: trova il primo carattere unico
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1
