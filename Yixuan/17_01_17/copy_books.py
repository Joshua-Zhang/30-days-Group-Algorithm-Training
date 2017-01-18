class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    # @author: Egbert Li
    # @link: http://www.lintcode.com/en/problem/copy-books/
    def copyBooks(self, pages, k):
        if len(pages) == 0:
            return 0
        max, total = 0, 0
        for page in pages:
            if page > max:
                max = page
            total += page
        start, end = max, total
        while start + 1 < end:
            mid = int (start + (end - start) / 2)
            if self.countCopiers(pages, mid) > k:
                start = mid
            else:
                end = mid
        if self.countCopiers(pages, start) <= k:
            return start
        return end

    def countCopiers(self, pages, limit):
        if len(pages) == 0:
            return 0
        sum, copiers = 0, 1
        for i in range(len(pages)):
            if sum + pages[i] > limit:
                sum = 0
                copiers += 1
            sum += pages[i]
        return copiers

        
