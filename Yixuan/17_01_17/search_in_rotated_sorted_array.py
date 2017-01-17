class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    @author: Egbert Li
    @link: http://www.lintcode.com/en/problem/search-in-rotated-sorted-array/
    """
    def search(self, A, target):
        if len(A) == 0:
            return -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            elif A[mid] > A[start]:
                if target >= A[start] and target < A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if target > A[mid] and target <= A[end]:
                    start = mid
                else:
                    end = mid
        if target == A[start]:
            return start
        elif target == A[end]:
            return end
        else:
            return -1
