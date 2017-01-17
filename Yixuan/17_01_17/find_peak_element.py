class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    #@link: http://www.lintcode.com/en/problem/find-peak-element/
    #@author: Egbert Li
    #$tag: Google
    def findPeak(self, A):
        if len(A) == 0:
            return 0
        while start + 1 < end:
            mid = int (start + (end - start) / 2)
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                start = mid
        if A[start] > A[end]:
            return start
        return end
