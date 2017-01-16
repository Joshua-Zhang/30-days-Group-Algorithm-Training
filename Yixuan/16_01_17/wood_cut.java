public class Solution {
    /**
     * @param L: Given n pieces of wood with length L[i]
     * @param k: An integer
     *return: The maximum length of the small pieces.
     * @link: http://www.lintcode.com/en/problem/wood-cut/#
     * @author: Egbert Li
     */
   public int woodCut(int[] L, int k) {
      int max = 0;
      for (int i = 0; i < L.length; i++) {
         max = Math.max(max, L[i]);
      }

      // find the largest length that can cut into k pieces
      int start = 1;
      int end = max;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         if (count(L, mid) < k) {
            end = mid;
         } else {
            start = mid;
         }
      }
      if (count(L, end) >= k) {
         return end;
      } else if (count(L, start) >= k) {
         return start;
      } else {
         return 0;
      }
   }

   private int count(int[] L, int length) {
      int total = 0;
      for (int i = 0; i < L.length; i++) {
         total += L[i] / length;
      }
      return total;
   }
}
