class Solution {
    /**
     * @param nums: A list of integer which is 0, 1 or 2
     * @return: nothing
     * @author: Egbert Li
     * @link: http://www.lintcode.com/en/problem/sort-colors/
     * @Tag : Facebook
     */
   public void sortColors(int[] nums) {
      if (nums == null || nums.length == 0) {
         return;
      }
      int i = 0, left = 0, right = nums.length - 1;
      while (i <= right) {
         if (nums[i] == 0) {
            swap(nums, left, i);
               left++;
               i++;
            } else if (nums[i] == 1) {
               i++;
            } else {
               swap(nums, i, right);
               right--;
            }
      }
   }

   private void swap(int[] nums, int left, int right) {
      if (nums.length == 0) {
         return;
      }
      int temp = nums[left];
      nums[left] = nums[right];
        nums[right] = temp;
    }
}
