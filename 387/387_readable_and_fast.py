# Variante leggibile: cerca tutte le lettere uniche e restituisce l'indice minimo
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = "abcdefghijklmnopqrstuvwxyz"
        listUniqueIndex = []
        for i in words:
            if s.count(i) == 1:
                listUniqueIndex.append(s.index(i))
        if len(listUniqueIndex) != 0:
            return min(listUniqueIndex)
        else:
            return -1
