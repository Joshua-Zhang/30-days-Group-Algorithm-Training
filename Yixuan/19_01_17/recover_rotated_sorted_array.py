class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    @link: http://www.lintcode.com/en/problem/recover-rotated-sorted-array/
    @author: Egbert Li
    """
    def recoverRotatedSortedArray(self, nums):
        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                self.reverse(nums, 0, index)
                self.reverse(nums, index + 1, len(nums) - 1)
                self.reverse(nums,0, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
