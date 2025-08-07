class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_length=200
        for s in strs:
            min_length = min(min_length,len(s))
        aux = []
        for i in range(min_length):
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    return "".join(aux)
                if(j+1 == len(strs)-1):
                    aux.append(strs[j+1][i])
            if(len(strs)==1):
                aux.append(strs[0][i])
        return "".join(aux)