class Solution{
public:
    /**
     * @param nums: A list of integer which is 0, 1 or 2
     * @return: nothing
     * @author: Egbert Li
     * @link: http://www.lintcode.com/en/problem/sort-colors/
     * @Tag: Facebook
     */
    void sortColors(vector<int> &nums) {
        if (nums.size() == 0) {
            return;
        }
        int start = 0, end = nums.size() - 1, index = 0;
        while (index <= end) {
            if (nums[index] == 0) {
                swap(nums[start], nums[index]);
                start++;
                index++;
            } else if (nums[index] == 1) {
                index++;
            } else {
                swap(nums[index], nums[end]);
                end--;
            }
        }
    }
};
