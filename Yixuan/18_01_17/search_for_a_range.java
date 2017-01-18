public class Solution {
    /**
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *@link http://www.lintcode.com/en/problem/search-for-a-range/
     *@author Egbert Li
     *return : a list of length 2, [index1, index2]
     */
	public int[] searchRange(int[] A, int target) {
		if (A.length == 0 || A == null) {
			return new int[]{-1,-1};
		}
		int[] range = new int[2];

		// get lower boundary
		int start, end, mid;
		start = 0;
		end = A.length - 1;
		while (start + 1 < end) {
			mid = start + (end - start) / 2;
			if (target == A[mid]) {
				end = mid;
			} else if (target < A[mid]) {
				end = mid;
			} else {
				start = mid;
			}
		}
		if (A[start] == target) {
			range[0] = start;
		} else if (A[end] == target) {
			range[0] = end;
		} else {
			range[0] = range[1] = -1;
			return range;
		}

		// get upper boundary
		start = 0;
		end = A.length - 1;
		while (start + 1 < end) {
			mid = start + (end - start) / 2;
			if (target == A[mid]) {
				start = mid;
			} else if (target < A[mid]) {
				end = mid;
			} else {
				start = mid;
			}
		}
		if (target == A[end]) {
			range[1] = end;
		} else if (target == A[start]) {
			range[1] = start;
		} else {
			range[0] = range[1] = -1;
			return range;
		}
		return range;
	}
}
