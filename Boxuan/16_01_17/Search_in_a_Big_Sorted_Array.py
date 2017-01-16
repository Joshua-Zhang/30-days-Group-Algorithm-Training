class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, A, target):
        if not A:
            return -1
        right = 0

        while right < len(A) and A[right] < target:
            right *= 2
            right += 1
        if right >= len(A):
            right = len(A) - 1
        
        left = 0
        while left + 1 < right:
            mid = left + (right - left) / 2
            if A[mid] < target:
                left = mid
            else:
                right = mid

        if A[left] == target:
            return left
        if A[right] == target:
            return right
            
        return -1

        