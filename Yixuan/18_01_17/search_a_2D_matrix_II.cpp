class Solution {
public:
    /**
     * @param matrix: A list of lists of integers
     * @param target: An integer you want to search in matrix
     * @return: An integer indicate the total occurrence of target in the given matrix
     * @author: Egbert Li
     * @link : http://www.lintcode.com/en/problem/search-a-2d-matrix-ii/#
     */
   int searchMatrix(vector<vector<int> > &matrix, int target) {
      int row = matrix.size();
      if (row == 0) {
         return 0;
      }
      int column = matrix[0].size();
      if (column == 0) {
         return 0;
      }
      int x = row - 1;
      int y = 0;
      int count = 0;
      while (x >= 0 && y <= colun - 1) {
         if (target == matrix[x][y]) {
            count ++;
            x --;
            y ++;
         } else if (target > matrix[x][y]) {
            y ++;
         } else {
            x --;
         }
      }
      return count;
   }
};
