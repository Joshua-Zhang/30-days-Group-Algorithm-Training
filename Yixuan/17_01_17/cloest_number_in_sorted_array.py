class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    # @author: Egbert Li
    # @link: http://www.lintcode.com/en/problem/closest-number-in-sorted-array/
    def closestNumber(self, A, target):
        if len(A) == 0:
            return 0
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if target == A[mid]:
                return mid
            elif target < A[mid]:
                end = mid
            else:
                start = mid
        if target - A[start] <= A[end] - target:
            return start
        else:
            return end
