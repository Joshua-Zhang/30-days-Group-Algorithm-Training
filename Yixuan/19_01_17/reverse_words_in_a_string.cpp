#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    /**
     * @param s : A string
     * @return : A string
     * @link : http://www.lintcode.com/en/problem/reverse-words-in-a-string/#
     * @author : Egbert Li
     */
    string reverseWords(string s) {
        int i = s.length() - 1;
        string ss;
        while (i >= 0) {
            while (i >= 0 && s[i] == ' ') {
                i --;
            }
            if (i < 0) break;
            if (ss.length() != 0) {
                ss.push_back(' ');
            }
            string temp;
            while (i >= 0 && s[i] != ' ') {
                temp.push_back(s[i]);
                i --;
            }
            reverse(temp.begin(), temp.end());
            ss.append(temp);
        }
        s = ss;
        return s;
    }
};
