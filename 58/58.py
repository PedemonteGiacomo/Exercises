# https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        end = len(s) - 1
        count = 0
        while end >= 0:
            if s[end] == " ":
                if count > 0:
                    break
            else:
                count += 1
            end -= 1
        return count
