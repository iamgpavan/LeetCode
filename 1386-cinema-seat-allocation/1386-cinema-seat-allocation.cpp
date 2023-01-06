class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        unordered_map<int, int> hm;
        unordered_map<int, int> count = {{7,2}, {6,1}, {5,0}, {4,1}, {3,1}, {2,1}, {1,1}, {0,0}};
        
        for(int i=0; i<reservedSeats.size(); i++){
            int seat = reservedSeats[i][1];
            int row = reservedSeats[i][0];
            if(hm.find(row) == hm.end()){
                hm[row] = 7;
            }
            
            if(seat == 3 || seat == 2){
                hm[row] = hm[row]&3;
            }else if(seat == 8 || seat == 9){
                hm[row] = hm[row]&6;
            }else if(seat >3 && seat <8){
                if(seat >= 6){
                    hm[row] = hm[row]&6;
                }else{
                    hm[row] = hm[row]&3;
                }
                hm[row] = hm[row]&5;
            }
        }
        int ans = (n-hm.size())*2;
        
        for(auto& it: hm){
            //cout << it.first << it.second << "\n";
            ans += count[it.second];
        }
        
        return ans;
    }
};