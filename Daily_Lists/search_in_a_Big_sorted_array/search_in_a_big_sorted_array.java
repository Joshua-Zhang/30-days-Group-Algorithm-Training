/**
 * Definition of ArrayReader:
 *
 * class ArrayReader {
 *      // get the number at index, return -1 if index is less than zero.
 *      public int get(int index);
 * }
 */
public class Solution {
    /**
     * @param reader: An instance of ArrayReader.
     * @param target: An integer
     * @return : An integer which is the index of the target number
     * @link: http://www.lintcode.com/en/problem/search-in-a-big-sorted-array/
     * @author: Egbert Li
     */
    public int searchBigSortedArray(ArrayReader reader, int target) {
        int index = 1;
        while (target > reader.get(index - 1)) {
            index *= 2;
        }
        int start = 0;
        int end = index - 1;
        while (start + 1 < end) {
            int mid = start + (end -start) / 2;
            if (target > reader.get(mid)) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (target == reader.get(start)) {
            return start;
        } else if (target == reader.get(end)) {
            return end;
        } else {
            return -1;
        }
    }
}
