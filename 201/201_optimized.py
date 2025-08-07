# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/

class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # Trova il prefisso comune tra left e right in binario
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        # Ricostruisci il risultato spostando a sinistra il prefisso comune
        return left << shift
            