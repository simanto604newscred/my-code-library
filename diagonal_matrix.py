class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        row = len(matrix)  # number of rows
        try:
            column = len(matrix[0])  # number of columns
        except Exception:
            column = 0

        result = []

        signal = 0
        i = 0
        j = 0

        while i < row and j < column:

            result.append(matrix[i][j])
            if signal == 0:

                if j == column-1:
                    i = i+1
                    signal = 1
                    continue
                if i == 0:
                    signal = 1
                    j=j+1
                    continue


                i=i-1
                j=j+1

            else:

                if i == row-1:
                    signal = 0
                    j = j+1
                    continue

                if j == 0:
                    signal = 0
                    i =i+1
                    continue

                i=i+1
                j=j-1

        return result










        return result



