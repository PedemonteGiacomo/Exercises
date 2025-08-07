# https://leetcode.com/problems/isomorphic-strings/
# Soluzione ottimizzata O(n) con doppia mappatura e commenti

class Solution(object):
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Per essere isomorfi:
        - Ogni carattere di s deve mappare su uno solo di t
        - Ogni carattere di t deve ricevere la mappatura da uno solo di s
        """
        if len(s) != len(t):
            return False
        map_s = {}  # s -> t
        map_t = {}  # t -> s
        for cs, ct in zip(s, t):
            # Se la mappatura esiste, deve essere coerente
            if cs in map_s and map_s[cs] != ct:
                return False
            if ct in map_t and map_t[ct] != cs:
                return False
            map_s[cs] = ct
            map_t[ct] = cs
        return True

# Esempi di test
if __name__ == "__main__":
    s = Solution()
    print(s.isIsomorphic("egg", "add"))      # True
    print(s.isIsomorphic("foo", "bar"))      # False
    print(s.isIsomorphic("paper", "title"))  # True
    print(s.isIsomorphic("ppaper", "tittle"))# False
    print(s.isIsomorphic("gge", "add"))      # False
