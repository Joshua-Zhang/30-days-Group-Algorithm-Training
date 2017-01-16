









# First Version
class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        else:
            return source.find(target)
