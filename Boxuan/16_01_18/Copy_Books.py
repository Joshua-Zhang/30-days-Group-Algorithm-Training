class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
        left, right = max(pages), sum(pages)
        while left + 1 < right:
            mid = left + (right - left) / 2
            if self.couterCopiers(pages, mid) > k:
                left = mid
            else:
                right = mid
        ans = left if self.couterCopiers(pages, left) < k else right
        return ans
        
    def couterCopiers(self, pages, limit):
        if not pages:
            return 0
        copier = 1
        sum = pages[0]
        for i in range(1, len(pages)):
            if sum + pages[i] > limit:
                sum = 0
                copier += 1
            sum += pages[i]
        return copier