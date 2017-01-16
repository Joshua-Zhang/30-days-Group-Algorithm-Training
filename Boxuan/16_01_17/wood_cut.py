class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if sum(L) < k:
            return 0
            
        left, right = 0, max(L)
        
        while left + 1 < right:
            mid = left + (right - left) / 2
            num_pieces = sum([wood / mid for wood in L])
            if num_pieces >= k:
                left = mid
            else:
                right = mid
                
        if sum([wood / right for wood in L]) >= k:
            return right   #make sure return the laggest length
            
        return left