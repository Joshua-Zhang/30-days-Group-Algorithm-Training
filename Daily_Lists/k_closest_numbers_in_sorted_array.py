Given a target number, a non-negative integer k
and an integer array A sorted in ascending order,
find the k closest numbers to target in A, sorted
in ascending order by the difference between the
number and target. Otherwise, sorted in ascending
order by number if the difference is same.

Have you met this question in a real interview? Yes
Example
Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].

Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

Challenge
O(logn + k) time complexity.


# C++
class Solution {
public:
    /**
     * @param A an integer array
     * @param target an integer
     * @param k a non-negative integer
     * @return an integer array
     */
    vector<int> kClosestNumbers(vector<int>& A, int target, int k) {
        // Write your code here
    }
};


# Python
class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @param {int} k a non-negative integer
    # @return {int[]} an integer array
    def kClosestNumbers(self, A, target, k):

        
