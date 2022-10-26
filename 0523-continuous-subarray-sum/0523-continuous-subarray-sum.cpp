class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> hm;
	    int sum = 0;
	    hm[0] = -1;
        
	    for(int i=0; i<nums.size(); i++){
	        sum += nums[i];
	        int rem = sum%k;
	        
	         
	        if(hm.find(rem) != hm.end() && i-hm[rem]>1)
	            return true;
	        
            if(hm.find(rem) == hm.end())   
                hm[rem] = i;
	        
	    }
	    
	    return false;
    }
};