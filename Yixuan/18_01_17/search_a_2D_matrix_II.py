class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    @link: http://www.lintcode.com/en/problem/search-a-2d-matrix-ii/#
    @author: Egbert Li
    """
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        if row == 0:
            return 0
        column = len(matrix[0])
        if column == 0:
            return 0
        count = 0
        x = row - 1
        y = 0
        while x >= 0 and y <= column - 1:
            if target == matrix[x][y]:
                count += 1
                x -= 1
                y -= 1
            elif target > matrix[x][y]:
                y += 1
            else:
                x -= 1
        returnh count
