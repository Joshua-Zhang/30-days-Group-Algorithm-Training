class Solution {
public:
    /**
     * @param A an integer array sorted in ascending order
     * @param target an integer
     * @return an integer
     * @link: http://www.lintcode.com/en/problem/closest-number-in-sorted-array/
     * @author : Egbert Li
     */
    int closestNumber(vector<int>& A, int target) {
        int length = A.size();
        if (length == 0) {
            return 0;
        }
        int start = 0;
        int end = length - 1;

        // get the closest number, aka the minimum number compare to target
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (target == A[mid]) {
                return mid;
            } else if (target < A[mid]) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (target - A[start] <= A[end] - target) {
            return start;
        } else {
            return end;
        }
    }
};
