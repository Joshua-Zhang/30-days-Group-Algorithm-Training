class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        
        # if not nums:
        #     return -1
        # for index, num in enumerate(nums):
        #     if num == target:
        #         return index
        #     if num > target:
        #         return -1
        
        left, right = 0, len(nums)
        
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
                
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
            
        return -1