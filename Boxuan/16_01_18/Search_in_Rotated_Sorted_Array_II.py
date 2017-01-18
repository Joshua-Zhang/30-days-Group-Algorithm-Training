class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        for index, num in enumerate(nums):
            if num == target:
                return True
        return False