/**
 * Definition of ArrayReader:
 *
 * class ArrayReader {
 * public:
 *     int get(int index) {
 *          // return the number on given index,
 *          // return -1 if index is less than zero.
 *     }
 * };
 */
class Solution {
public:
    /**
     * @param reader: An instance of ArrayReader.
     * @param target: An integer
     * @return: An integer which is the first index of target.
     * @author: Egbert Li
     * @link: http://www.lintcode.com/en/problem/search-in-a-big-sorted-array/
     */
    int searchBigSortedArray(ArrayReader *reader, int target) {
        int index = 1;
        while (target > reader->get(index - 1)) {
            index *= 2;
        }
        int start = 0;
        int end = index - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (target > reader->get(mid)) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (target == reader->get(start)) {
            return start;
        } else if (target == reader->get(end)) {
            return end;
        } else {
            return -1;
        }
    }
};
