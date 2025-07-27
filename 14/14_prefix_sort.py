class Solution(object):
    def longestCommonPrefix(self, strs):
        # Se la lista è vuota, non c'è prefisso comune
        if not strs:
            print("Input vuoto. Nessun prefisso comune.")
            return ""
        # Ordina l'array: il prefisso comune tra tutte le stringhe sarà quello tra la prima e l'ultima
        strs.sort()
        print(f"Ordinato: {strs}")
        first = strs[0]
        last = strs[-1]
        print(f"first: {first}")
        print(f"last: {last}")
        i = 0
        # Confronta carattere per carattere tra la prima e l'ultima stringa
        while i < len(first) and i < len(last) and first[i] == last[i]:
            print(f"i={i}: {first[i]} == {last[i]}")
            i += 1
        if i < len(first) and i < len(last):
            print(f"i={i}: {first[i]} != {last[i]} (stop)")
        print(f"Prefisso comune: '{first[:i]}'")
        # Il prefisso comune è la sottostringa fino al primo carattere diverso
        return first[:i]


if __name__ == "__main__":
    s = Solution()
    # Esempio 1
    print("\nEsempio 1:")
    input1 = ["flower", "flow", "flight"]
    print(f"Input: {input1}")
    print("Risultato:", s.longestCommonPrefix(input1))

    # Esempio 2
    print("\nEsempio 2:")
    input2 = ["dog", "racecar", "car"]
    print(f"Input: {input2}")
    print("Risultato:", s.longestCommonPrefix(input2))

    # Esempio 3
    print("\nEsempio 3:")
    input3 = ["interspace", "internet", "internal", "interval"]
    print(f"Input: {input3}")
    print("Risultato:", s.longestCommonPrefix(input3))

    # Esempio 4 (input vuoto)
    print("\nEsempio 4:")
    input4 = []
    print(f"Input: {input4}")
    print("Risultato:", s.longestCommonPrefix(input4))
