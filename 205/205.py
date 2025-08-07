# https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s: str, t: str):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_t = {}
        for i in range(len(s)):
            if map_t.get(s[i],"") == "" or map_t.get(s[i],"") == t[i]:
                for key in map_t:
                    if map_t[key] == t[i] and map_t.get(s[i],"") == "":
                        return False
                map_t[s[i]] = t[i]
            else:
                return False
        return True
            