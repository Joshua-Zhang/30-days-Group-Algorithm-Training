public class Solution {
    /**
     * @param s : A string
     * @return : A string
     * @link: http://www.lintcode.com/en/problem/reverse-words-in-a-string/#
     * @author: Egbert Li
     */
    public String reverseWords(String s) {
        if (s.length() == 0 || s == null) {
            return "";
        }
        StringBuilder sb  = new StringBuilder();
        String[] array = s.split(" ");
        for (int i = array.length - 1; i >= 0; i--) {
            if (!array[i].equals("")) {
                sb.append(array[i]).append(" ");
            }
        }
        // remove the last " "
        return sb.length() == 0 ? "" : sb.substring(0, sb.length() - 1);
    }
}
