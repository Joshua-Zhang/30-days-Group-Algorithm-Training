class Solution {
public:
    /**
     * @param A an integer array sorted in ascending order
     * @param target an integer
     * @return an integer
     * @link: http://www.lintcode.com/en/problem/last-position-of-target/
     * @author: Egbert Li
     */
    int lastPosition(vector<int>& A, int target) {
      int length = A.size();
      if (length == 0) {
         return -1;
      }
      int start = 0;
      int end = A.size() - 1;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         if (target < A[mid]) {
            end = mid;
         } else {
            start = mid;
         }
      }
      if (target == A[end]) {
         return end;
      } else if (target == A[start]) {
         return start;
      } else {
         return -1;
      }
    }
};
