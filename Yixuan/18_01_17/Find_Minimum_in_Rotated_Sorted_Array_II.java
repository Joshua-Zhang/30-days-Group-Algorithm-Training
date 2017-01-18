public class Solution {
    /**
     * @param num: a rotated sorted array
     * @return: the minimum number in the array
     */
   public int findMin(int[] nums) {
      if (nums.length == 0 && nums == null) {
         return -1;
      }
      int start = 0;
      int end = nums.length - 1;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         // if mid equals to end, that means it's fine to remove end
         // the smallest element won't be removed
         if (nums[mid] == nums[end]) {
            end --;
         } else if (nums[mid] < nums[end]) {
            end = mid;
         } else {
            start = mid;
         }
      }
      if (nums[start] <= nums[end]) {
         return nums[start];
      }
      return nums[end];
   }
}
