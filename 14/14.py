# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # calcolo la lunghezza massima per la quale posso iterare nel caso peggiore
        min_lenght = len(min(strs, key=len))
        aux = []
        for i in range(min_lenght):
            prev_char = strs[0][i]
            for str in strs[1:]:
                this_char = str[i]
                if prev_char != this_char:
                    return "".join(aux)
            aux.append(prev_char)
            print("".join(aux))
        return "".join(aux)