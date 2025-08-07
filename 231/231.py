# https://leetcode.com/problems/power-of-two/
import math

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 2 != 0 and n != 1 or n <= 0:
            return False # un numero dispari non può essere sicuramente una potenza di 2
        res = int(math.log(n, 2))
        return pow(2,res) == n or pow(2,res) == 1 # 1 se 2^0 = 1