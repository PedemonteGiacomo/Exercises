# https://leetcode.com/problems/valid-anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        occurencies = {}
        for char in s:
            occurencies[char] = occurencies.get(char,0) + 1
        for char in t:
            occurencies[char] = occurencies.get(char,-1) -1
        for key in occurencies:
            if occurencies[key] != 0:
                return False
        return True
