# https://leetcode.com/problems/pascals-triangle/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        start = [1]
        rows = []
        rows.append(start)
        if numRows == 1:
            return rows
        righe_fatte = 1
        while righe_fatte < numRows:
            prev_row = rows[-1]
            len_prev_row = len(prev_row)
            for i in range(len_prev_row):
                if i+1 == len_prev_row:                
                    start.append(prev_row[i])
                    # sono arrivato in fondo della prev_row
                    rows.append(start)
                    start = [1]
                else:
                    sum_ = prev_row[i] + prev_row[i+1]
                    start.append(sum_)
            righe_fatte += 1
        return rows
