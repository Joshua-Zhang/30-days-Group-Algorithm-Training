class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    # @link: http://www.lintcode.com/en/problem/last-position-of-target/
    # @author: Egbert Li
    def lastPosition(self, A, target):
        if len(A) == 0:
            return -1
        start = 0
        end = len(A) - 1
        while start + 1< end:
            mid = int(start + (end - start) / 2 )
            if target < A[mid]:
                end = mid
            else:
                start  = mid
        if target == A[end]:
            return end
        elif target == A[start]:
            return start
        else:
            return -1
