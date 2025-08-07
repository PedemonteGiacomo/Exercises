# https://leetcode.com/problems/moving-average-from-data-stream/description/

from collections import deque

class MovingAverage(object):
    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size          # larghezza finestra
        self.q = deque()          # conserva al massimo 'size' elementi
        self.running_sum = 0      # somma degli elementi attuali

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        # se la q non è ancora grande quanto size non devo fare uscire niente e basta questo
        if(self.q.__len__()<self.size):
            self.q.append(val)
            self.running_sum+=val
        # altrimenti levo l'ultimo a sinistra, che era il più vecchio
        else:
            out=self.q.popleft()
            self.running_sum-=out
            self.running_sum+=val
            self.q.append(val)
        
        return self.running_sum/float(self.q.__len__())

            
#fammi vedere se funziona
if __name__ == "__main__":
    obj = MovingAverage(3)   # finestra di 3
    print(obj.next(1))       # [1]                  → media = 1.0
    print(obj.next(10))      # [1,10]               → (1+10)/2 = 5.5
    print(obj.next(3))       # [1,10,3]             → 14/3 = 4.6667
    print(obj.next(5))       # [10,3,5] (1 esce)    → 18/3 = 6.0