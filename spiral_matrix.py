__author__ = 'MAK'


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        result = []
        row_start = 0
        col_start = 0
        row_end = len(matrix)
        col_end = len(matrix[0])

        while row_start<row_end and col_start<col_end:

            for i in range(col_start, col_end):
                result.append(matrix[row_start][i])

            row_start += 1


            for i in range(row_start, row_end):
                result.append(matrix[i][col_end-1])

            col_end -= 1


            if row_start < row_end:
                for i in range(col_end-1, col_start-1,-1):
                    result.append(matrix[row_end-1][i])

                row_end -= 1

            if col_start < col_end:
                for i in range(row_end-1, row_start-1,-1):
                    result.append(matrix[i][col_start])

                col_start += 1


        return result

if __name__ == '__main__':
    Solution().spiralOrder([[3],[2]])
