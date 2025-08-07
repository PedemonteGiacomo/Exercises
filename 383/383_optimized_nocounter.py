# https://leetcode.com/problems/ransom-note/
# Soluzione ottimizzata O(n) senza Counter, solo dict standard

class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Ottimizzazione senza Counter:
        - Uso un dizionario normale per contare le lettere di magazine
        - Scorro ransomNote e consumo le lettere
        """
        count_magazine = {}
        for c in magazine:
            count_magazine[c] = count_magazine.get(c, 0) + 1
        for c in ransomNote:
            if count_magazine.get(c, 0) == 0:
                return False
            count_magazine[c] -= 1
        return True

# Esempi di test
if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("a", "b"))         # Output: False
    print(s.canConstruct("aa", "ab"))       # Output: False
    print(s.canConstruct("aa", "aab"))      # Output: True
