class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first å of target in nums, position start from 0
    # @author Egbert Li
    def binarySearch(self, nums, target):
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = int (start + (end - start) / 2)
            if target > nums[mid]:
                start = mid
            else:
                end = mid
        if target == nums[start]:
            return start
        elif target == nums[end]:
            return end
        else:
            return -1
