// Second Version
class Solution {
   /**
    * @param x: An integer
    * @return: The sqrt of x
    * @link: http://www.lintcode.com/en/problem/sqrtx/
    * @author: Egbert Li
    * @Tag: Facebook
    */
   public int sqrt(int x) {
      if (x <= 0) {
         return 0;
      }
      int start = 1;
      int end = x;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         if (mid == x / mid) {
            return mid;
         } else {
            // to avoid overflow
            if (x / mid < mid) {
               end = mid;
            } else {
               start = mid;
            }
         }
      }

      return start;
   }
}

// First Version
class Solution {
    /**
     * @param x: An integer
     * @return: The sqrt of x
     * @link: http://www.lintcode.com/en/problem/sqrtx/
     * @author: Egbert Li
     * @Tag: Facebook
     */
    public int sqrt(int x) {
        if (x == 0) {
            return 0;
        }
        long start = 1;
        long end = x;
        while (start + 1 < end) {
            long mid = start + (end - start) / 2;
            if (mid * mid  > x) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (end * end <= x && end >= start) {
            return (int) end;
        }
        return (int) start;
    }
}
