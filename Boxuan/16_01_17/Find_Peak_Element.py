class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
            
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid - 1]:
                right = mid - 1 
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
        ans = left if nums[left] > nums[right] else right
        return ans