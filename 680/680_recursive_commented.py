# https://leetcode.com/problems/valid-palindrome-ii/
# Versione ricorsiva con commenti dettagliati

class Solution(object):
    def validPalindrome(self, s):
        """
        Verifica se la stringa può diventare palindroma eliminando al massimo un carattere.
        :type s: str
        :rtype: bool
        """
        def helper(i, j, chance):
            # Scorriamo la stringa con due indici, uno dall'inizio (i) e uno dalla fine (j)
            while i < j:
                if s[i] != s[j]:
                    # Se troviamo una differenza e abbiamo già usato la possibilità di eliminare un carattere, non è valido
                    if chance == 0:
                        return False
                    # Proviamo a saltare il carattere a sinistra (i+1) oppure quello a destra (j-1)
                    # chance viene settato a 0 perché da qui in poi non possiamo più eliminare caratteri
                    return helper(i+1, j, 0) or helper(i, j-1, 0)
                # Se i caratteri sono uguali, avviciniamo i due indici
                i += 1
                j -= 1
            # Se usciamo dal ciclo senza trovare differenze, la stringa (o sottostringa) è palindroma
            return True
        # Avviamo la ricorsione con entrambi gli indici agli estremi e una possibilità di eliminazione
        return helper(0, len(s)-1, 1)
