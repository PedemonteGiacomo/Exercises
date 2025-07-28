# Soluzione O(n) ottimizzata con array per alfabeti limitati (solo lettere minuscole)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Se sappiamo che s contiene solo lettere minuscole, possiamo usare un array di 26 elementi
        freq = [0] * 26
        ord_a = ord('a')
        for char in s:
            freq[ord(char) - ord_a] += 1
        for i, char in enumerate(s):
            if freq[ord(char) - ord_a] == 1:
                return i
        return -1
