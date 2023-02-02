class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        unordered_map<int, int> hm;
        
        for(int i=0; i<order.size(); i++){
            hm[order[i]-'a'] = i;
        }
        
        for(int i=0; i<words.size()-1; i++){
            for(int j=0; j<words[i].size(); j++){
                if(j >= words[i+1].size())  return false;
                
                if(words[i][j] != words[i+1][j]){
                    if(hm[words[i][j]-'a'] > hm[words[i+1][j]-'a']) return false;
                    break;
                }
            }
        }
        
        return true;
    }
};