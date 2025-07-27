class Solution(object):
    def longestCommonPrefix(self, strs):
        # Se la lista è vuota, non c'è prefisso comune
        if not strs:
            return ""
        # zip(*strs) crea un iteratore che raggruppa i caratteri nella stessa posizione di tutte le stringhe
        # Esempio: ["car", "cat"] -> zip(*strs) = [('c','c'), ('a','a'), ('r','t')]
        for i, chars in enumerate(zip(*strs)):
            # set(chars) crea un insieme dei caratteri in posizione i: se sono diversi, la lunghezza sarà > 1
            if len(set(chars)) > 1:
                # Appena troviamo una differenza, restituiamo il prefisso fino a quel punto
                return strs[0][:i]
        # Se non troviamo differenze, il prefisso comune è lungo quanto la stringa più corta
        return min(strs, key=len)