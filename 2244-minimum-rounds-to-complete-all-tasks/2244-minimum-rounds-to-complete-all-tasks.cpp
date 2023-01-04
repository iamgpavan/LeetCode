class Solution {
public:
    int minimumRounds(vector<int>& tasks) {
        unordered_map<int, int> hm;
        
        for(int i=0; i<tasks.size(); i++){
            if(hm.find(tasks[i])!=hm.end()){
                hm[tasks[i]] += 1;
            }else{
                hm[tasks[i]] = 1;
            }
        }
        
        int ans = 0;
        
        for(auto& it:hm){
            int value = it.second;
            if(value == 1)  return -1;
            
            while(value > 3){
                value -= 3;
                ans += 1;
            }
            
            if(value)   ans += 1;            
        }
        
        return ans;
    }
};