class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int sum = 0;
        for(int i=0; i<k; i++){
            sum += nums[i];
        }
        
        int curr_sum = sum;
        
        for(int i=k; i<nums.size(); i++){
            curr_sum = curr_sum - nums[i-k] + nums[i];
            
            if(curr_sum > sum){
                sum = curr_sum;
            }
        }
        
        return (double)sum/k;
    }
};