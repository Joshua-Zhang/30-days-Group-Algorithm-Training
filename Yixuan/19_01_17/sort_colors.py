class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    @link: http://www.lintcode.com/en/problem/sort-colors/
    @author: Egbert Li
    @Tag: Facebook
    """
    def sortColors(self, nums):
        if len(nums) == 0:
            return
        index, left, right = 0, 0, len(nums) - 1
        while index <= right:
            if nums[index] == 0:
                self.swap(nums, left, index)
                left += 1
                index += 1
            elif nums[index] == 1:
                index += 1
            else:
                self.swap(nums, index, right)
                right -= 1


    def swap(self, nums, left, right):
        if len(nums) == 0:
            return
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
