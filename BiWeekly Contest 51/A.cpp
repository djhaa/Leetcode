class Solution {
public:
    char get(char c, int len){
        return c + len;
    }

    string replaceDigits(string s) {
        for(int i = 0; i < s.size(); i++){
            if(i & 1){
                s[i] = get(s[i-1], s[i] - '0');
            }
        }
        return s;
    }
};