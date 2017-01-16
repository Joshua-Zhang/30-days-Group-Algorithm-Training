Given a big sorted array with positive integers
sorted by ascending order. The array is so big so that
 you can not get the length of the whole array directly,
 and you can only access the kth number by ArrayReader.
 get(k) (or ArrayReader->get(k) for C++).
 Find the first index of a target number.
 Your algorithm should be in O(log k),
 where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

 Notice

If you accessed an inaccessible index (outside of the array),
 ArrayReader.get will return 2,147,483,647.


Example
Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.

Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.

Challenge
O(log k), k is the first index of the given target number.

Tags
Binary Search Facebook Uber

# C++ Start

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
     */
    int searchBigSortedArray(ArrayReader *reader, int target) {

    }
};

# Java Start
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
     */
    public int searchBigSortedArray(ArrayReader reader, int target) {

    }
}

# Python Start
"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
