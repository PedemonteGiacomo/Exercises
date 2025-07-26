
# https://leetcode.com/problems/minimum-window-substring/description/
class Solution(object):
    def allCharactersInAstring(self, s, t):
        count_s = {}
        count_t = {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        for char in count_t:
            if count_s.get(char, 0) < count_t[char]:
                return False
        return True

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        print(f"Input s: {s}, t: {t}")
        if n > m or not self.allCharactersInAstring(s,t):
            print("Condizione di base non soddisfatta: t non in s o t più lunga di s")
            return ""
        starting_lenght = n
        left = 0
        right = starting_lenght
        length = starting_lenght
        while length <= m:
            print(f"Window: s[{left}:{right}] -> '{s[left:right]}' (length={length})")
            print(s[left:right])
            if self.allCharactersInAstring(s[left:right],t):
                print(f"Trovata sottostringa valida: '{s[left:right]}'")
                return s[left:right]
            if right == m:
                length += 1
                left = 0
                print(f"Aumento lunghezza window a {length}")
            else:
                left += 1
            right = left + length
        print("Nessuna sottostringa trovata, ritorno tutta la stringa s")
        return s
            

if __name__ == "__main__":
    s = "ab"
    t = "b"
    sol = Solution()
    result = sol.minWindow(s, t)
    print(f"Risultato finale: '{result}'")