# https://leetcode.com/problems/minimum-window-substring/description/

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Dizionario per contare i caratteri richiesti da t
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1
        # Variabili per la finestra
        left = 0  # inizio della finestra
        min_len = float('inf')  # lunghezza minima trovata
        min_start = 0  # inizio della finestra minima
        have = {}  # caratteri trovati nella finestra
        count = 0  # quanti caratteri di t sono soddisfatti nella finestra
        # Scorri la stringa s con right
        for right in range(len(s)):
            char = s[right]
            # Aggiorna il conteggio dei caratteri nella finestra
            have[char] = have.get(char, 0) + 1
            # Se il carattere è richiesto e la quantità è giusta, aumenta count
            if char in need and have[char] == need[char]:
                count += 1
            # Quando tutti i caratteri richiesti sono nella finestra
            while count == len(need):
                # Aggiorna la finestra minima se serve
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                # Prova a restringere la finestra da sinistra
                left_char = s[left]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    count -= 1
                left += 1
        # Se non è stata trovata nessuna finestra valida, restituisci stringa vuota
        if min_len == float('inf'):
            return ""
        # Altrimenti restituisci la sottostringa minima trovata
        return s[min_start:min_start + min_len]

# Esempio di test con commenti di debug
if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    result = sol.minWindow(s, t)
    print(f"Risultato finale: '{result}'")
    # Output atteso: 'BANC'
