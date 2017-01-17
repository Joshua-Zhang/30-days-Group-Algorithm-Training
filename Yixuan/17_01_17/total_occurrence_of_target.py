class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    # @link: http://www.lintcode.com/en/problem/total-occurrence-of-target/
    # @author: Egbert Li
    def totalOccurrence(self, A, target):
        if len(A) == 0:
            return 0
        if target < A[0]:
            return 0
        if target > A[len(A) - 1]:
            return 0

        start = 0
        end = len(A) - 1
        # get lower bound first, if start != end != target, return 0
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if target > A[mid]:
                start = mid
            else:
                end = mid
        if target == A[start]:
            left = start
        elif target == A[end]:
            left = end
        else:
            return 0

        # get upper bound
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2 )
            if target < A[mid]:
                end = mid
            else:
                start = mid
        if target == A[end]:
            right = end
        else:
            right = start
        return right - left + 1
