class Solution {
    public int singleNonDuplicate(int[] nums) {
        if(nums.length==1)
        return nums[0];
        int low = 0, high = nums.length-1;
        while(low<=high){
            int mid = low+(high-low)/2;
            if((mid>0&&mid<nums.length-1&&nums[mid]!=nums[mid-1]&&nums[mid]!=nums[mid+1])||(mid==0&&nums[mid]!=nums[mid+1])||(mid==nums.length-1&&nums[mid]!=nums[mid-1]))
            return nums[mid];
            if(mid%2==0){
                if(mid!=0&&nums[mid]==nums[mid-1]){
                    high = mid-1;
                }else{
                    low=mid+1;
                }
            }else{
                if(mid!=0&&nums[mid]==nums[mid-1]){
                    low = mid+1;
                }else{
                    high=mid-1;
                }
            }
        }
        return -1;
    }
}