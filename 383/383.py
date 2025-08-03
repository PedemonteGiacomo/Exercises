# https://leetcode.com/problems/ransom-note/

class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count_ransomNote = {}
        count_magazine = {}
        for c in ransomNote:
            count_ransomNote[c] = count_ransomNote.get(c,0) + 1
        for c in magazine:
            count_magazine[c] = count_magazine.get(c,0) + 1
        for c in ransomNote:
            if count_magazine.get(c,0) < count_ransomNote[c]:
                return False
        return True