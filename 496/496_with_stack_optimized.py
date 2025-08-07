# https://leetcode.com/problems/next-greater-element-i/
# Soluzione ottimizzata O(N+M) con monotonic stack e dizionario
# Commenti passo-passo per capire la logica

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        Per ogni elemento di nums2, trova il suo 'next greater' a destra
        Usa uno stack per tenere i numeri in attesa di un maggiore
        """
        next_greater = {}  # Dizionario: num -> suo next greater
        stack = []         # Stack monotono decrescente
        # Scorri nums2 da sinistra a destra
        for num in nums2:
            # Se il numero corrente è maggiore di quello in cima allo stack
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num  # Il next greater di prev è num
            stack.append(num)
        # Gli elementi rimasti nello stack non hanno un next greater
        while stack:
            prev = stack.pop()
            next_greater[prev] = -1
        # Costruisci la risposta per nums1
        return [next_greater[num] for num in nums1]

# Esempio di test
if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElement([4,1,2], [1,3,4,2]))  # Output: [-1,3,-1]
    print(s.nextGreaterElement([2,4], [1,2,3,4]))    # Output: [3,-1]
