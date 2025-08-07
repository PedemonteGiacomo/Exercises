# https://leetcode.com/problems/valid-anagram
# Constraint: s and t consist of lowercase English letters only

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Se le lunghezze sono diverse, non possono essere anagrammi
        if len(s) != len(t):
            return False
        # Usa un array di 26 elementi per contare le occorrenze di ogni lettera
        count = [0] * 26
        for i in range(len(s)):
            # ord('a') = 97, quindi ord(s[i]) - ord('a') va da 0 a 25
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        # Se tutte le posizioni sono 0, sono anagrammi
        for c in count:
            if c != 0:
                return False
        return True

# Esempi di test
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
    print(sol.isAnagram("aabbcc", "abcabc"))    # True
    print(sol.isAnagram("aabbcc", "aabbc"))     # False
