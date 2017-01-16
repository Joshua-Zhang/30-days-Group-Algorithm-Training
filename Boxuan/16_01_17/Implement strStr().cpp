class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.length();
        int n = needle.length();
        if (m == 0 and n == 0){
            return 0;
        }
        for(int i = 0; i <= m + 1; i++){
            for(int j = 0; j <= n + 1; j++){
                                
                if (j == n){
                    return i;
                }
                
                if (i + j == m){
                    return - 1;
                }

                if (haystack[i + j] != needle[j]) {
                    break;
                }
            }
        }
    }
};