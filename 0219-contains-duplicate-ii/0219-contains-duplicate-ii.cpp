class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> hm;
        
        for(int i=0; i<nums.size(); i++){
            if(hm.find(nums[i]) != hm.end()){
                if(abs(i-hm[nums[i]]) <= k) return true;
            }
            hm[nums[i]] = i;
        }
        
        return false;
    }
};