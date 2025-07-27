# https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_bits = str(bin(n)[2:])  # Convert to binary and remove '0b' prefix
        count = 0
        for char in str_bits:
            if char == '1':
                count += 1
        return count