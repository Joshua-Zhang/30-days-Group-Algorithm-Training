class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return 0
        row, col = len(matrix) - 1, 0
        counter = 0
        while col < len(matrix[0]) and row >= 0:
            if matrix[row][col] == target:
                row -= 1
                col += 1
                counter += 1
            elif matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
        return counter