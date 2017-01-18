class Solution {
public:
    int findMin(vector<int>& nums) {
        if (nums.size() == 0){
            return 0;
        }
        int left = 0;
        int right = nums.size() - 1;
        
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (nums[right] <= nums[mid]){
                left = mid;
            }else{
                right = mid;
            }
        }
        return min(nums[right], nums[left]);
    }
};