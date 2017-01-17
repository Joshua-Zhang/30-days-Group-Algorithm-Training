class Solution {
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     * @author : Egbet Li
     * @link: http://www.lintcode.com/en/problem/find-peak-element/
     */
   public int findPeak(int[] A) {
      if (A.length == 0) {
         return 0;
      }
      int start = 0;
      int end = A.length - 1;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         if (A[mid] < A[mid - 1]) {
            end = mid;
         } else if (A[mid] < A[mid + 1]) {
            start = mid;
         } else {
            start = mid;
         }
      }
      if (A[start] > A[end]) {
         return start;
      }
      return end;
   }
}
