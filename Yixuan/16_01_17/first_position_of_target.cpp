class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target number to find.
     * @return: The first position of target. Position starts from 0.
     * @author: Egbert Li
     */
public:
	int binarySearch(vector<int> &array, int target) {
      int array_length = array.size();
      if (array_length == 0) {
         return -1;
      }
      int start = 0;
      int end = array_length - 1;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         if (target > array[mid]) {
            start = mid;
         } else {
            end = mid;
         }
      }
      if (target == array[start]) {
         return start;
      } else if (target == array[end]) {
         return end;
      } else {
         return -1;
      }
	}
};
