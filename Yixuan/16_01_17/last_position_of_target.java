public class Solution {
    /**
     * @param nums: An integer array sorted in ascending order
     * @param target: An integer
     * @return an integer
     * @link: http://www.lintcode.com/en/problem/last-position-of-target/
     * @author : Egbert Li
     */
    public int lastPosition(int[] nums, int target) {
      if (nums.length == 0) {
         return -1;
      }
      int start = 0;
      int end = nums.length - 1;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         if (target < nums[mid]) {
            end = mid;
         } else {
            start = mid;
         }
      }
      if (target == nums[end]) {
         return end;
      } else if (target == nums[start]) {
         return start;
      } else {
         return -1;
      }
    }
}
