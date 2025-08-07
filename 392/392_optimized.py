# https://leetcode.com/problems/is-subsequence/description/

class Solution(object):
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        last_index = -1
        for c in s:
            # Cerca c in t dopo last_index
            last_index = t.find(c, last_index + 1)
            if last_index == -1:
                return False
        return True