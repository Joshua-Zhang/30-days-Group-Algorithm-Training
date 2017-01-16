"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    # @author: Egbert Li
    # @link: http://www.lintcode.com/en/problem/search-in-a-big-sorted-array/
    def searchBigSortedArray(self, reader, target):
        index = 1
        while target > reader.get(index - 1):
            index *= 2
        start = 0
        end = index - 1
        while start + 1 < end:
            mid = start + int((end - start) / 2)
            if target > reader.get(mid):
                start = mid
            else:
                end = mid
        if target == reader.get(start):
            return start
        elif target == reader.get(end):
            return end
        else:
             return -1
