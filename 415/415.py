# https://leetcode.com/problems/add-strings/description/

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # idea: parto dal fondo della stringa e converto quel carattere in int e lo sommo con i carattere in fondo dell'altra stringa, sse ci sono riporti li devo considerae per il prossimo passo
        num1 = str(num1)
        num2 = str(num2)
        end_num_1 = len(num1)-1
        end_num_2 = len(num2)-1
        carry = 0
        res = []
        while end_num_1 >= 0 or end_num_2 >= 0 or carry == 1:
            calc = (int(num1[end_num_1]) if end_num_1 >= 0 else 0) + (int(num2[end_num_2]) if end_num_2 >= 0 else 0) + carry
            carry = calc // 10
            res.append(str(calc % 10))
            end_num_1 -= 1
            end_num_2 -= 1
        res.reverse()  # perché ho aggiunto i caratteri in ordine inverso
        return ''.join(res)