public class Solution {
    /**
     * @param nums: The rotated sorted array
     * @return: void
     * @link: http://www.lintcode.com/en/problem/recover-rotated-sorted-array/
     * @author: Egbert Li
     */
   public void recoverRotatedSortedArray(ArrayList<Integer> nums) {
      for (int index = 0; index < nums.size() - 1; index++) {
         if (nums.get(index) > nums.get(index + 1)) {
            reverse(nums, 0, index);
            reverse(nums, index + 1, nums.size() - 1);
            reverse(nums, 0, nums.size() - 1);
         }
      }
   }

   private void reverse(ArrayList<Integer> nums, int start, int end) {
      while (start < end) {
         int temp = nums.get(start);
         nums.set(start, nums.get(end));
         nums.set(end, temp);
         start ++;
         end --;
      }
   }
}
