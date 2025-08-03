# https://leetcode.com/problems/is-subsequence/description/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        last_index = [0]
        for i in range(len(s)):
            index_to_find = t.find(s[i], last_index[-1])
            if index_to_find == -1:
                return False
            else:
                last_index.append(index_to_find)
        return True