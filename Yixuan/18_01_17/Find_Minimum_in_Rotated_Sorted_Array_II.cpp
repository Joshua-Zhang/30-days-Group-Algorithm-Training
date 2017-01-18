class Solution {
public:
    /**
     * @param num: the rotated sorted array
     * @return: the minimum number in the array
     * @link: http://www.lintcode.com/en/problem/find-minimum-in-rotated-sorted-array-ii/
     * @author: Egbert Li
     */
    int findMin(vector<int> &num) {
        int length = num.size();
        if (length == 0) {
            return -1;
        }
        int start = 0;
        int end = length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (num[mid] == num[end]) {
                end--;
            } else if (num[mid] < num[end]) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (num[start] <= num[end]) {
            return num[start];
        } else {
            return num[end];
        }
    }
};
