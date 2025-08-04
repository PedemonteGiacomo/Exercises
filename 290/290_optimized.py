# https://leetcode.com/problems/word-pattern/
# Soluzione ottimizzata O(n) con doppia mappatura e commenti

class Solution(object):
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Verifica se la sequenza di parole segue il pattern dato.
        - Ogni carattere del pattern deve mappare su una sola parola
        - Ogni parola deve ricevere la mappatura da un solo carattere
        """
        words = s.split()
        if len(words) != len(pattern):
            return False
        map_p = {}  # pattern -> word
        map_w = {}  # word -> pattern
        for p, w in zip(pattern, words):
            if p in map_p and map_p[p] != w:
                return False
            if w in map_w and map_w[w] != p:
                return False
            map_p[p] = w
            map_w[w] = p
        return True

# Esempi di test
if __name__ == "__main__":
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat dog"))  # True
    print(s.wordPattern("abba", "dog cat cat fish")) # False
    print(s.wordPattern("aaaa", "dog cat cat dog"))  # False
    print(s.wordPattern("abba", "dog dog dog dog"))  # False
