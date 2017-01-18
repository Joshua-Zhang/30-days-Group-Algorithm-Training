public class Solution {
    /**
     * @param n an integer
     * @return an integer
     * @link : http://www.lintcode.com/en/problem/drop-eggs/
     * @author: Egbert Li
     */
    public int dropEggs(int n) {
        long ans = 0;
        int x = 0; // asume start from Xth flooer
        while (ans < n) {
            x += 1;
            ans += x;
        }
        return x;
    }
}
