class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total = 0;
        int gas_sum = 0;
        int cost_sum=  0;
        int ans = 0;
        
        for(int i=0; i<gas.size(); i++){
            total += (gas[i]-cost[i]);
            gas_sum += gas[i];
            cost_sum += cost[i];
            
            if(total < 0){
                total = 0;
                ans = i+1;
            }
        }
        
        if(gas_sum < cost_sum)  return -1;
        
        return ans;
    }
};