class Solution {
public:
    /**
     * @param pages: a vector of integers
     * @param k: an integer
     * @return: an integer
     * @link: http://www.lintcode.com/en/problem/copy-books/
     * @author: Egbert Li
     */
   int copyBooks(vector<int> &pages, int k) {
      int length = pages.size();
      if (length == 0) {
         return 0;
      }
      int max = pages[0], total = 0;
      for (int i = 0; i < length; i++) {
         total += pages[i];
         if (pages[i] > max) {
            max = pages[i];
         }
      }
      int start = max;
      int end = total;
      while (start + 1 < end) {
         int mid = start + (end - start) / 2;
         if (countCopiers(pages, mid) > k) {
            start = mid;
         } else {
            end = mid;
         }
      }
      if (countCopiers(pages, start) <= k) {
         return start;
      }
      return end;
   }
// according the current pages get possible people to copy
private:
   int countCopiers(vector<int> &pages, int limit) {
      if (pages.size() == 0) {
          return 0;
      }
      int sum = pages[0];
      int copiers = 1;
      for (int i = 1; i < pages.size(); i++) {
         if (sum + pages[i] > limit) {
            sum = 0;
            copiers++;
         }
         sum += pages[i];
      }
      return copiers;
   }
};
