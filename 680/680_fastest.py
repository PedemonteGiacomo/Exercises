# https://leetcode.com/problems/valid-palindrome-ii/
# Soluzione più veloce e compatta possibile in Python (O(n)), con commenti dettagliati

class Solution(object):
    def validPalindrome(self, s):
        """
        Verifica se la stringa può diventare palindroma eliminando al massimo un carattere.
        Utilizza due puntatori e slicing solo in caso di mismatch.
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                # Se troviamo una differenza, proviamo a saltare il carattere a sinistra (i) oppure a destra (j)
                # e controlliamo se una delle due sottostringhe è palindroma tramite slicing e confronto con il reverse
                return s[i+1:j+1] == s[i+1:j+1][::-1] or s[i:j] == s[i:j][::-1]
            # Se i caratteri sono uguali, avviciniamo i due indici
            i += 1
            j -= 1
        # Se non troviamo differenze, la stringa è già palindroma
        return True
