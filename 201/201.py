class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # parto da left fino ad arrivare a right
        bin_str_left = str(bin(left))
        bin_str_right = str(bin(right))
        len_left = len(bin_str_left)
        len_right = len(bin_str_right)
        if len_left < len_right:
            return 0
        res = left
        while left < right:
            left += 1
            res &= left
            if res == 0:
                return res
        return res