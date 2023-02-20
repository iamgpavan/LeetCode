class Solution {
public:
   int searchInsert(vector<int>& nums, int t) {
        if(t<=nums[0])
          return 0;
        if(t==nums[nums.size()-1])
          return nums.size()-1;
        if(t>nums[nums.size()-1])
          return nums.size();
        if(nums.size()==2 && nums[0]<t && nums[1]>t)
          return 1;
        
        int i=1,j=nums.size()-2,mid;

        while(i<=j){
            mid=(i+j)/2;
            if(nums[mid-1]<t && nums[mid]>=t)
              return mid;
            else if(nums[mid]<t && nums[mid+1]>=t)
              return mid+1;
            else if(nums[mid]<t)
              i=mid+1;
            else 
              j=mid-1;
        }
        return -1;
    }
};