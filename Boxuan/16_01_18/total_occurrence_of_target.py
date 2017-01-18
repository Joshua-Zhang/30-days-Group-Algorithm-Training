# Python
class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    # @link: http://www.lintcode.com/en/problem/total-occurrence-of-target/
    # @author: Egbert Li
    def totalOccurrence(self, A, target):
        if not A:
            return 0
        
        left, right = 0, len(A) - 1

#search the first left index of target
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] < target:
                left = mid
            else:
                right = mid
        left_index = left if A[left] == target else right
        if left_index != target:
            return -1
#search the first right index of target

        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] > target:
                right = mid
            else:
                left = mid
        right_index = right if A[right] == target else left

        return abs(right_index - left_index) + 1