public class Solution {
    /**
     * @param A an integer array sorted in ascending order
     * @param target an integer
     * @return an integer
     * @link: http://www.lintcode.com/en/problem/total-occurrence-of-target/
     * @author: Egbert Li
     */
    public int totalOccurrence(int[] A, int target) {
        if (A.length == 0 || A == null) {
            return 0;
        }
        int start = 0;
        int end = A.length - 1;
        int right = 0;
        int left = 0;

        // get the left bound
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (target > A[mid]) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (target == A[start]) {
            left = start;
        } else if (target == A[end]) {
            left = end;
        } else {
            return 0;
        }

        // get the right bound
        start = 0;
        end = A.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (target < A[mid]) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (target == A[end]) {
            right = end;
        } else {
            right = start;
        }


        return right - left + 1;
    }
}
