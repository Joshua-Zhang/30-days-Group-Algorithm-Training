class Solution {
public:
    int mySqrt(int x) {
        // write your code here
        long left = 0;
        if (x == 1)
            return 1;
        long right = x;
        
        while (left+1 < right) {
            long mid = left + (right-left)/2;
            if (x > mid*mid) {
                left = mid;
            } else if (x < mid*mid) {
                right = mid;
            } else {
                return mid;
            }
        }
        return left;
    }
};