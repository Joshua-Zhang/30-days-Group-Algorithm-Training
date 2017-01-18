class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    # @link: http://www.lintcode.com/en/problem/find-minimum-in-rotated-sorted-array-ii/
    # @author: http://www.lintcode.com/en/problem/find-minimum-in-rotated-sorted-array-ii/
    def findMin(self, num):
        if len(num) == 0:
            return -1
        start = 0
        end = len(num) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if num[mid] == num[end]:
                end -= 1
            elif num[mid] < num[end]:
                end = mid
            else:
                start = mid
        if num[start] <= num[end]:
            return num[start]
        else:
            return num[end]
