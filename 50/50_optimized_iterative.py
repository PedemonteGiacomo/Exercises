# Se n è 0, restituisci 1 (caso base).
# Se n è negativo, calcola la potenza con l’esponente positivo e poi fai il reciproco (1/risultato).
# Se n è pari, calcola (x^2)^(n/2).
# Se n è dispari, calcola x * (x^(n-1)).
# "Exponentiation by Squaring"
class Solution(object):
    def myPow(self, x, n):
        # Caso base: qualsiasi numero elevato a 0 fa 1
        if n == 0:
            return 1
        # Se n è negativo, calcoliamo la potenza con esponente positivo e poi faremo il reciproco
        reciproco = n < 0
        n = abs(n)
        result = 1  # Inizializziamo il risultato a 1 (neutro della moltiplicazione)
        while n:
            # Se l'esponente è dispari, moltiplichiamo il risultato per x
            if n % 2 == 1:
                result *= x
            # Eleviamo x al quadrato (x = x^2) per la prossima iterazione
            x *= x
            # Dividiamo l'esponente per 2 (parte intera): ci spostiamo al bit successivo
            n //= 2
        # Se l'esponente originale era negativo, restituiamo il reciproco
        return 1/result if reciproco else result