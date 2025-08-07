# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # prima di tutto rendo la s in minuscolo
        s = str(s)
        s = s.lower()
        # mi devo tenere solo i valori alfanumerici
        s_clean = []
        for char in s:
            if char.isalnum():
                s_clean.append(char)
        s="".join(s_clean)
        print(s)
        # muovo due puntatori, uno da inizio e uno da fine
        # se i caratteri sono uguali vado avanti altrimenti esco
        end = len(s) - 1
        half = end + 1 // 2 # prendo la metà come divisione intera (es. 13/2 = 6)
        start = 0
        while start < half:
            if s[start] != s[end]:
                return False
            else:
                #vado avanti
                start += 1
                end -= 1
        return True