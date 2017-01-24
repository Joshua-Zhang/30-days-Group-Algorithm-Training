class Solution {
public:
    /**
     * @param str: a string
     * @param offset: an integer
     * @return: nothing
     */
   void rotateString(string &str,int offset){
      if (str.size() == 0) {
         return;
      }
      offset = offset % str.size();
      str = str.substr(str.size() - offset, offset) +
            str.substr(0, str.size() - offset);
   }
};
