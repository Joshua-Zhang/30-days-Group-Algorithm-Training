class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    # @author: Egbert Li
    # @link: http://www.lintcode.com/en/problem/closest-number-in-sorted-array/
    def closestNumber(self, A, target):
        if not target:
            return -1
        left, right = 0, len(target) -1 
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                left = mid
            else:
                right = mid
        ans = left if abs(A[left] - target) < abs(A[right] - target) else right
        return ans