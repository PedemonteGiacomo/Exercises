# https://leetcode.com/problems/valid-anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        occurencies = {}
        n = len(s)
        m = len(t)
        if n != m:
            return False
        for i in range(n):
            occurencies[s[i]] = occurencies.get(s[i],0) + 1
            occurencies[t[i]] = occurencies.get(t[i],0) - 1
        for key in occurencies:
            if occurencies[key] != 0:
                return False
        return True

# Esempi di test, inclusi casi Unicode
if __name__ == "__main__":
    sol = Solution()
    # Caso base
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
    # Caso con caratteri maiuscoli
    print(sol.isAnagram("Listen", "Silent"))    # False (case sensitive)
    # Caso con caratteri Unicode
    print(sol.isAnagram("àèì", "ìèà"))          # True
    print(sol.isAnagram("café", "face"))        # False
    # Caso con emoji
    print(sol.isAnagram("😀😃😄", "😄😀😃"))      # True
