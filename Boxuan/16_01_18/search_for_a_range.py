class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]
            
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] > target:
                right = mid
            else:
                left = mid
        right_index = right if A[right] == target else left
        if A[right_index] != target:
            return [-1, -1]
            
        left, right = 0, len(A)
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] < target:
                left = mid
            else:
                right = mid
        left_index = left if A[left] == target else right
        
        return [left_index, right_index]