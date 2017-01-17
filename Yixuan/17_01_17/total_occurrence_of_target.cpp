class Solution {
public:
    /**
     * @param A an integer array sorted in ascending order
     * @param target an integer
     * @return an integer
     * @link: http://www.lintcode.com/en/problem/total-occurrence-of-target/
     * @author: Egbert Li
     */
    int totalOccurrence(vector<int>& A, int target) {
       int length = A.size();
       if (length == 0) {
           return 0;
       }
       if (target > A[length - 1] || target < A[0]) {
           return 0;
       }
       int left = 0;
       int right = 0;
       int start = 0;
       int end = length - 1;
       // get lower bound, if A[start] != A[end] != target, then return 0
       while (start + 1 < end) {
           int mid = start + ((end - start) >> 1);
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

       // get upper bound
       start = 0;
       end = length - 1;
       while (start + 1 < end) {
           int mid = start + ((end - start) >> 1);
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
       return  right - left + 1;
    }
};
