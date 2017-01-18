class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    # @link: http://www.lintcode.com/en/problem/divide-two-integers/
    # @author: Egbert Li
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        a = dividend > 0 ? dividend : -dividend
        b = divisor > 0 ? divisor : -divisor
        result, shift = 0, 31
        while shift >= 0:
            if a >= (b << shift):
                a -= b << shift
                result += b << shift
            shift -= 1
        if (dividend ^ divisor) >> 31:
            result = -result
        if result > INT_MAX:
            return INT_MAX
        return result
        
