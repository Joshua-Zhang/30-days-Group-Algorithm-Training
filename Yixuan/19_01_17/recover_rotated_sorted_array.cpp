class Solution {
    /**
     * @param nums: The rotated sorted array
     * @return: void
     * @link: http://www.lintcode.com/en/problem/recover-rotated-sorted-array/
     * @author: Egbert Li
     */
public:
   void recoverRotatedSortedArray(vector<int> &nums) {
      int length = nums.size();
      for (int index = 0; index < length - 1; index++) {
         if (nums[index] > nums[index + 1]) {
            reverse(nums, 0, index);
            reverse(nums, index + 1, length - 1);
            reverse(nums, 0, length - 1);
         }
      }
   }

private:
   void reverse(vector<int> &nums, int start, int end) {
      while (start < end) {
         int temp = nums[start];
         nums[start] = nums[end];
         nums[end] = temp;
         start ++;
         end --;
      }
   }
};
