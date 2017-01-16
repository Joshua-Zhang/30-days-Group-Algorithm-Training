class Solution {
    /**
     * Returns a index to the first occurrence of target in source,
     * or -1  if target is not part of source.
     * @param source string to be scanned.
     * @param target string containing the sequence of characters to match.
     * @link: http://www.lintcode.com/en/problem/strstr/
     * @author: Egbert Li
     * @Tag: Facebook, Phone interview questions
     */
   public int strStr(String source, String target) {
      if (source == null || target == null) {
         return -1;
      }
      int source_length = source.length();
      int target_length = target.length();
      for (int i = 0; i < source_length - target_length + 1; i++) {
         int j = 0;
         for (j = 0; j < target_length; j++) {
            if (source.charAt(i + j) !=  target.charAt(j)) {
               break;
            }
         }
         if (j == target_length) {
            return i;
         }
      }
      return -1;
   }
}
