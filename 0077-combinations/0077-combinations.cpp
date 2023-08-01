class Solution {
public:
    void subseq(int n,vector<int> temp,int i,int k,vector<vector<int>>& ans){
        if(temp.size()==k && i==n+1){
            ans.push_back(temp);
            return;
        }
        if((temp.size() + (n-i+1))<k){
            return;
        }
        if(i==n+1 && temp.size()!=k){
            return;
        }
        subseq(n,temp,i+1,k,ans);
        temp.push_back(i);
        subseq(n,temp,i+1,k,ans);
    }
    vector<vector<int>> combine(int n, int k) {

        vector<int> temp;

        vector<vector<int>> ans;

        subseq(n,temp,1,k,ans);

        return ans;

    }
};