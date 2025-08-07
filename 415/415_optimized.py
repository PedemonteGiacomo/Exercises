# https://leetcode.com/problems/add-strings/description/

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        end_num_1 = len(num1) - 1
        end_num_2 = len(num2) - 1
        carry = 0
        res = []
        while end_num_1 >= 0 or end_num_2 >= 0 or carry:
            n1 = int(num1[end_num_1]) if end_num_1 >= 0 else 0
            n2 = int(num2[end_num_2]) if end_num_2 >= 0 else 0
            calc = n1 + n2 + carry
            carry = calc // 10
            res.append(str(calc % 10))
            end_num_1 -= 1
            end_num_2 -= 1
        return ''.join(res[::-1])
