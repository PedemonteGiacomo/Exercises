# https://leetcode.com/problems/ransom-note/
# Soluzione ottimizzata O(n) spazio O(1) usando un solo dizionario
# Ragionamento: scorro magazine e "consumo" le lettere necessarie

class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Ottimizzazione:
        - Uso un solo dizionario per contare le lettere disponibili in magazine
        - Scorro ransomNote e "consumo" le lettere dal dizionario
        - Se manca una lettera, ritorno subito False
        - Così risparmio spazio e tempo
        """
        from collections import Counter
        count_magazine = Counter(magazine)
        for c in ransomNote:
            if count_magazine[c] == 0:
                return False
            count_magazine[c] -= 1  # Consuma la lettera
        return True

# Esempi di test
if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("a", "b"))         # Output: False
    print(s.canConstruct("aa", "ab"))       # Output: False
    print(s.canConstruct("aa", "aab"))      # Output: True
