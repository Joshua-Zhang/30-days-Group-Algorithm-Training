public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @param: A number you want to search in the matrix
     * @return: An integer indicate the occurrence of target in the given matrix
     */
    public int searchMatrix(int[][] matrix, int target) {
      if (matrix.length == 0 || matrix == null) {
         return 0;
      }
      if (matrix[0].length == 0 || matrix[0] == null) {
         return 0;
      }
      int row = matrix.length;
      int column = matrix[0].length;
      int x = row - 1;
      int y = 0;
      int occurrence = 0;
      while (x >= 0 && y <= column - 1) {
         int curr_num = matrix[x][y];
         if (target == curr_num) {
            occurrence++;
            x--;
            y++;
         } else if (target > curr_num) {
            y++;
         } else {
            x--;
         }
      }
      return occurrence;
    }
}
