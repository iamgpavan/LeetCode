class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int N = nums.size();
        vector<int> ans(2);
        
        for(int i=0; i<N; i++){
            nums[i] += N;
        }
        
        for(int i=0; i<N; i++){
            //cout<<nums[i] << " ** " << "\n";
            nums[(nums[i])%(N+1)] += N+1;
            //cout<<nums[i] << " ** ";
        }
        
        for(int i=0; i<N; i++){
            //cout<<nums[i] << " ** ";
            nums[i]-=N+1;
            nums[i]/=N+1;
        }
        
        for(int i=0; i<N; i++){
            //cout<<nums[i] << " ** ";
             if(nums[i] > 1) ans[0] = i+1;
            if(nums[i] == 0)    ans[1] = i+1;
        }
        
        
        return ans;
    }
};