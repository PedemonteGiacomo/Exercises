# https://leetcode.com/problems/powx-n/

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        reciproco = False
        if n < 0:
            reciproco = True
            n=abs(n)
        res = x
        while n > 1:
            res *= x
            n -= 1
        print(res)
        if reciproco:
            res = 1/res
        return res