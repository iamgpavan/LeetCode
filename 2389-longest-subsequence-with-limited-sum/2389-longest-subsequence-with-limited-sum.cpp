class Solution {
public:
    int binarySearch(vector<int> nums, int key){
        int start = 0;
        int end = nums.size()-1;
        int count = 0;
        
        while(start <= end){
            int mid = (start + end)/2;
            
            if(nums[mid] <= key){
                count = mid+1;
                start = mid + 1;
            }else{
                end = mid - 1;
            }
        }
        
        return count; 
    }
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());
        
        vector<int> ans;
        
        for(int i=1; i<nums.size(); i++){
            nums[i] += nums[i-1];
        }
        
        for(int i=0; i<queries.size(); i++){
            ans.push_back(binarySearch(nums, queries[i]));
        }
        
        return ans;
    }
};