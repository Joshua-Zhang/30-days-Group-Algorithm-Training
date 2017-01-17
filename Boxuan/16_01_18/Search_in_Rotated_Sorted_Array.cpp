class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while (left + 1 < right){
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[left]){
                if (nums[mid] >= target and nums[left] <= target){
                    right = mid;
                }else{
                    left = mid;
                }
            }else{
                if (nums[mid] <= target and nums[right] >= target){
                    left = mid;
                }else{
                    right = mid;
                }
            }
        }
        if (nums[left] == target){
            return left;
        }
        if (nums[right] == target){
            return right;
        }
        return -1;
    }
};