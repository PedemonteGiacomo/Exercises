# https://leetcode.com/problems/valid-palindrome-ii/

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def helper(i, j, chance):
            while i < j:
                if s[i] != s[j]:
                    if chance == 0:
                        return False
                    # Prova a saltare uno dei due caratteri
                    return helper(i+1, j, 0) or helper(i, j-1, 0)
                i += 1
                j -= 1
            return True
        return helper(0, len(s)-1, 1)
