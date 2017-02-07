class Solution:
    # @param s : A string
    # @return : A string
    # @author: Egbert Li
    # @link: http://www.lintcode.com/en/problem/reverse-words-in-a-string/
    def reverseWords(self, s):
        return " ".join(reversed(s.strip().split(" ")))
