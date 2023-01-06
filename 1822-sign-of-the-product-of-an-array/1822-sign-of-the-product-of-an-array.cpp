class Solution {
public:
    int arraySign(vector<int>& nums) {
        int ans = 0;
        
        for(int i=0; i<nums.size(); i++){
            if((nums[i]<0 && ans == -1) || (nums[i] > 0 && ans!=-1)){
                ans = 1;
            }else if(nums[i] == 0){
                return 0;
            }else{
                ans = -1;
            }
            //cout << nums[i] << " " << ans << "\n";
        }
        
        return ans;
    }
};