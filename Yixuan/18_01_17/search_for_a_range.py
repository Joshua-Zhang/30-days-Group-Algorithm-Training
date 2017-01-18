class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    @author: Egbert Li
    @link: http://www.lintcode.com/en/problem/search-for-a-range/
    """

    def searchRange(self, A, target):
	if len(A) == 0:
		return [-1, -1]

	# get lower bound
	start = 0
	end = len(A) - 1
	while start + 1 < end:
		mid = start + (end - start) / 2
		if target > A[mid]:
			start = mid
		else:
			end = mid
	if target == A[start]:
		left_bound = start
	elif target == A[end]:
		left_bound = end
	else:
		return [-1, -1]

	# get the upper bound
	start = 0
	end = len(A) - 1
	while start + 1 < end:
		mid = start + (end - start) / 2
		if target < A[mid]:
			end = mid
		else:
			start = mid
	if target == A[end]:
		right_bound = end
	else:
		right_bound = start
	return [left_bound, right_bound]
