class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomeSet = set(ransomNote)
        for c in ransomeSet:
            if ransomNote.count(c)> magazine.count(c):
                return False
        return True