class Solution {
public:
    bool detectCapitalUse(string word) {
        bool first_cap = false;
        if(word[0] >= 'A' and word[0]<='Z')   first_cap = true;
        int cap_count = 0;
        for(int i=1; i<word.size(); i++){
            if(word[i] >= 'A' and word[i]<='Z')   cap_count += 1;
        }
        
        if(first_cap && (cap_count == 0 || cap_count == word.size()-1)) return true;
        else if(cap_count == 0) return true;
        
        return false;
    }
};