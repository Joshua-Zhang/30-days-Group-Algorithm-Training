public class Solution {
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     * @link: http://www.lintcode.com/en/problem/find-minimum-in-rotated-sorted-array/
     * @author: Egbert Li
     */
   public int findMin(int[] nums) {
      if (nums.length == 0) {
         return 0;
      }
      int start = 0;
      int end = nums.length - 1;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         if (nums[mid] > nums[end]) {
            start = mid;
         } else {
            end = mid;
         }
      }
      if (nums[start] < nums[end]) {
         return nums[start];
      }
      return nums[end];
   }
}
