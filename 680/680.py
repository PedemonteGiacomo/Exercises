# https://leetcode.com/problems/valid-palindrome-ii/

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # scorro dall'inizio e dalla fine
        # tengo un contatore di caratteri diversi, se è maggiore di 2 restituisco false, altrimenti true
        s = str(s)
        start = 0
        end = len(s) - 1
        half = end + 1 // 2
        count = 0
        while start < half:
            if s[start] != s[end]:
                # ho due strade adesso, stringa senza s[start] o stringa senza s[end], 
                # se una sola delle due è palindroma allora siamo apposto
                # posso verificarlo facendo il confronto con il reverse delle stringhe
                without_start = s[:start] + s[start+1:]
                without_end = s[:end] + s[end+1:]
                reverse_without_start = without_start[::-1]
                reverse_without_end = without_end[::-1]
                if without_start == reverse_without_start or without_end == reverse_without_end:
                    return True
                else:
                    return False
            start += 1
            end -= 1
        return True