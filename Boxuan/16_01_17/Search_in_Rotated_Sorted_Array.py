class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[left]:
                if nums[left] <= target and nums[mid] >= target:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target and nums[right] >= target:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1