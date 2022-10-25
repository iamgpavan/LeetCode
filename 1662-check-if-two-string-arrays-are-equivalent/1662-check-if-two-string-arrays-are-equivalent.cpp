class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        int i=0;
        int j=0;
        int x=0,y=0;
        
        while(i<word1.size() && j<word2.size()){
            while(x<word1[i].length() && y<word2[j].length()){
                if(word1[i][x] != word2[j][y])  return false;
                x += 1;
                y += 1;
            }
            
            if(x>=word1[i].length()){
                x = 0;
                i += 1;
            }
            
            if(y>=word2[j].length()){
                y = 0;
                j += 1;
            }
        }
       
        if(i!=word1.size() || j!=word2.size())    return false;
        return true;
    }
};