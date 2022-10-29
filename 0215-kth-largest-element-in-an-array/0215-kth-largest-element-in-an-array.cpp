class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue <int, vector<int>, greater<int>> pq;
        
        int i=0;
        
        while(i<nums.size()){
            if(pq.size() < k){
                pq.push(nums[i]);
            }else if(pq.top() < nums[i]){
                pq.pop();
                pq.push(nums[i]);
            }
            i+=1;
        }
        
        return pq.top();
    }
};