class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @param {int} k a non-negative integer
    # @return {int[]} an integer array
    def kClosestNumbers(self, A, target, k):
        # Write your code here
        if not A or k == 0:
            return []

        res = []
        index = self.binarySearch(A, target)
        res.append(A[index])
        k -= 1
        left, right = index - 1, index + 1
        while k > 0:
            if left >= 0 and right <= len(A) - 1:
                if abs(A[left] - target) <= abs(A[right] - target):
                    res.append(A[left])
                    left -= 1
                    k -= 1
                else:
                    res.append(A[right])
                    right += 1
                    k -= 1
            if left < 0:
                while k > 0 and right <= len(A) - 1:
                    res.append(A[right])
                    right += 1
                    k -= 1
                break
            if right > len(A) - 1:
                while k > 0 and left >= 0:
                    res.append(A[left])
                    left -= 1
                    k -= 1
                break
        return res


    def binarySearch(self, L, target):
        start, end = 0, len(L) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if L[mid] == target:
                return mid
            elif L[mid] > target:
                end = mid
            else:
                start = mid

        return start if abs(L[start] - target) <= abs(L[end] - target) else end