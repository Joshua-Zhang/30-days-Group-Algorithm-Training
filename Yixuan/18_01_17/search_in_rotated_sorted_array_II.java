public class Solution {
    /**
     * param A : an integer ratated sorted array and duplicates are allowed
     * param target :  an integer to be search
     * return : a boolean
     * link : http://www.lintcode.com/en/problem/search-in-rotated-sorted-array-ii/
     * author: Egbert Li
     */
   public boolean search(int[] A, int target) {
      if (A.length == 0 || A == null) {
         return 0;
      }
      int start = 0;
      int end = A.length - 1;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         if (target == A[mid]) {
            return true;
         } else if (target < A[end]) {

         }
      }
   }
}







// Version 1
public class Solution {
    /**
     * param A : an integer ratated sorted array and duplicates are allowed
     * param target :  an integer to be search
     * return : a boolean
     * link : http://www.lintcode.com/en/problem/search-in-rotated-sorted-array-ii/
     * author: Egbert Li
     */
    public boolean search(int[] A, int target) {
        if (A.length == 0 || A == null) {
            return false;
        }
        for (int i = 0; i < A.length; i++) {
            if (target == A[i]) {
                return true;
            }
        }
        return false;
    }
}
