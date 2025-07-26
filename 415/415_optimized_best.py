# https://leetcode.com/problems/add-strings/description/

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Inizializza i puntatori agli ultimi caratteri di num1 e num2
        i, j = len(num1) - 1, len(num2) - 1
        # Inizializza il riporto a 0
        carry = 0
        # Lista per accumulare le cifre del risultato (in ordine inverso)
        res = []
        # Continua finché ci sono cifre da sommare o un riporto da gestire
        while i >= 0 or j >= 0 or carry:
            # Ottieni la cifra corrente di num1 (da destra), oppure 0 se terminata
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            # Ottieni la cifra corrente di num2 (da destra), oppure 0 se terminata
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            # Somma le due cifre e il riporto
            total = digit1 + digit2 + carry
            # Calcola il nuovo riporto per la prossima iterazione
            carry = total // 10
            # Aggiungi la cifra meno significativa del totale alla lista risultato
            res.append(str(total % 10))
            # Sposta i puntatori a sinistra (verso le cifre più significative)
            i -= 1
            j -= 1
        # Inverte la lista delle cifre e le unisce in una stringa finale
        return ''.join(reversed(res))
