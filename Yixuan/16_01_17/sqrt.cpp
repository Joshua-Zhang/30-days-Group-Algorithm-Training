class Solution {
public:
    /**
     * @param x: An integer
     * @return: The sqrt of x
     * @author: Egbert Li
     * @link: http://www.lintcode.com/en/problem/sqrtx/
     * @tag :Facebook
     */
    int sqrt(int x) {
        if (x <= 0) {
            return 0;
        }
        int start = 1;
        int end = x;
        while(start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (mid == x / mid) {
                return mid;
            } else {
                if (x / mid < mid) {
                    end = mid;
                } else {
                    start = mid;
                }
            }
        }
        return start;
    }
};
