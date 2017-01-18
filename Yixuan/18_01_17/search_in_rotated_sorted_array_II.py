class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    @link: http://www.lintcode.com/en/problem/search-in-rotated-sorted-array-ii/
    @author: Egbert Li
    """
    def search(self, A, target):
        if len(A) == 0:
            return False
        A = sorted(set(A))
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if target == A[mid]:
                return True
            elif target < A[mid]:
                end = mid
            else:
                start = mid
        if A[start] == target or A[end] == target:
            return True
        return False
