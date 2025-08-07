from typing import List
# https://leetcode.com/problems/reverse-string/

class Solution(object):
    def reverseString(self, s: List[str]) -> None:
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        start = 0
        n = len(s)
        end = n-1
        half = end + 1 // 2
        while start < half:
            aux = s[start]
            s[start] = s[end]
            s[end] = aux
            start += 1
            end -= 1
        return s
