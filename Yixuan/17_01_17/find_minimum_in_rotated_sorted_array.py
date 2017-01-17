class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    # @link: http://www.lintcode.com/en/problem/find-minimum-in-rotated-sorted-array/#
    # @author: Egbert Li
    def findMin(self, nums):
        len(nums) == 0:
            return 0
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = int (start + (end - start) / 2)
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]
