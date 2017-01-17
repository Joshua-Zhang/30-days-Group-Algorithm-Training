public class Solution {
    /**
     * @param A : an integer rotated sorted array
     * @param target :  an integer to be searched
     * @return : an integer
     * @link: http://www.lintcode.com/en/problem/search-in-rotated-sorted-array/
     * @author: Egbert Li
     */
   public int search(int[] A, int target) {
      if (A.length == 0) {
         return -1;
      }
      int start = 0;
      int end = A.length - 1;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         if (target == A[mid]) {
            return mid;
         } else if (A[mid] > A[start]) {
            if (target < A[mid] && target >= A[start]) {
               end = mid;
            } else {
               start = mid;
            }
         } else {
            if (target > A[mid] && target <= A[end]) {
               start = mid;
            } else {
               end = mid;
            }
         }
      }
      if (target == A[start]) {
         return start;
      }
      if (target == A[end]) {
         return end;
      }
      return -1;
   }
}
