class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int ans = 0;
        int nones = 0;
        
        for(int i=0; i<s.size(); i++){
            if(s[i] == '1') nones +=1;
            else if(nones  > 0){
                nones -= 1;
                ans += 1;
            }
        }
        
        return ans;
    }
};