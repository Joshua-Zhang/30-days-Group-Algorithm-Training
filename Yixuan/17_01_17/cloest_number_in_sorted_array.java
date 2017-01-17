public class Solution {
    /**
     * @param A an integer array sorted in ascending order
     * @param target an integer
     * @return an integer
     * @link: http://www.lintcode.com/en/problem/closest-number-in-sorted-array/
     * @author : Egbert Li
     */
   public int closestNumber(int[] A, int target) {
      if (A.length == 0) {
         return 0;
      }
      int start = 0;
      int end = A.length - 1;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         if (target == A[mid]) {
            return mid;
         } else if (target < A[mid]) {
            end = mid;
         } else {
            start = mid;
         }
      }
      if (target - A[start] <= A[end] - target) {
         return start;
      }
      return end;
   }
}
