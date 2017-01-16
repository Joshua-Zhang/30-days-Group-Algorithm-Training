class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    @link: http://www.lintcode.com/en/problem/sqrtx/
    @author: Egbert Li
    @tag: Facebook
    """
    def sqrt(self, x):
        if x <= 0:
            return 0
        start = 1
        end = x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        if end * end <= x and end >= start:
            return end
        return start
