# https://leetcode.com/problems/happy-number/

class Solution(object):
    def isHappy(self, n: int) -> bool:
        new_n=str(n)
        already_seen = {}
        while new_n != "1":
            sum = 0
            for char in new_n:
                char_num = int(char)
                sum += char_num*char_num
            new_n = str(sum)
            already_seen[new_n] = already_seen.get(new_n, 0) + 1
            if already_seen[new_n] > 1:
                return False
        return True


