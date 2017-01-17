#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    @author: Egbert Li
    @link: http://www.lintcode.com/en/problem/first-bad-version/
    """
    def findFirstBadVersion(self, n):
        if n <= 0:
            return 0
        start = 0
        end = n
        while start + 1 < end:
            mid = int (start + (end - start) / 2)
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid
        if SVNRepo.isBadVersion(start):
            return start
        return end
