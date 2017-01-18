class Solution {
public:
    /**
     * @param n an integer
     * @return an integer
     * @link: http://www.lintcode.com/en/problem/drop-eggs/
     * @author: Egbert Li
     */
    int dropEggs(int n) {
        long ans = 0;
        int x = 0;
        while (ans < n) {
            x += 1;
            ans += x;
        }
        return x;
    }
};
