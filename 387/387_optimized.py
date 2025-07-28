# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for char in s:
            count[char] = count.get(char,0)+1
        for key in count:
            if count[key] == 1:
                return s.find(key)
        return -1
