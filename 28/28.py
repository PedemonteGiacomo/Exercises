class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        if m > n:
            return -1

        # mappa indice → carattere di needle
        need = {i: ch for i, ch in enumerate(needle)}
        # mappa indice → carattere di haystack
        stack = {i: ch for i, ch in enumerate(haystack)}

        # scorriamo tutti i possibili punti di inizio
        for i in range(0, n - m + 1):
            # controlliamo prima carattere
            if stack[i] != need[0]:
                continue

            # proviamo a far combaciare tutti i successivi
            match = True
            for j in range(1, m):
                if stack.get(i + j) != need[j]:
                    match = False
                    break

            if match:
                return i

        return -1
