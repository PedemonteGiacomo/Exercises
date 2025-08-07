# https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n - 1  # Rimuove il bit meno significativo a 1
            count += 1
        return count