class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x
        
        while left + 1 < right:
            mid = left + (right - left) / 2
            if mid * mid == x:
                return mid
                
            elif mid * mid < x:
                left = mid
            
            else:
                right = mid 
                
                
        ans = right if right * right == x else left
        
        return ans