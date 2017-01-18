class Solution:
    # @param {int} n an integer
    # @return {int} an integer
    # @link: http://www.lintcode.com/en/problem/drop-eggs/
    # @author : Egbert Li
    def dropEggs(self, n):
        ans = 0
        x = 0
        while ans < n:
            x += 1
            ans += x
        return x
