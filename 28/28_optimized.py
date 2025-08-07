class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # edge case: needle vuoto
        if not needle:
            return 0

        n, m = len(haystack), len(needle)
        # scorri ogni possibile inizio in haystack
        for i in range(n - m + 1):
            # verifica se la sottostringa di lunghezza m combacia
            if haystack[i:i+m] == needle:
                return i
        return -1
