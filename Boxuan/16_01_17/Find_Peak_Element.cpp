class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if (nums.size() == 0){
            return -1;
        }
        int left = 0;
        int right = nums.size() - 1;
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]){
                return mid;
            }
            else if (nums[mid] > nums[mid + 1]){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        int ans = nums[right] > nums[left]?right:left;
        return ans;
    }
};