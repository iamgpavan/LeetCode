class Solution {
private:
    void dfs(int i, vector<int> graph[], vector<int> &vis){
        vis[i] = 1;
        
        for(auto it: graph[i]){
            if(!vis[it]){
                dfs(it, graph, vis);
            }
        }
    }
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        vector<int> graph[isConnected.size()];
        vector<int> vis(isConnected.size(), 0);
        
        for(int i=0; i<isConnected.size(); i++){
            for(int j=0; j<isConnected[0].size(); j++){
                if(isConnected[i][j] == 1){
                    graph[i].push_back(j);
                    graph[j].push_back(i);
                }
            }
        }
        
        int ans = 0;
        
        for(int i=0; i<isConnected.size(); i++){
            if(!vis[i]){
                ans += 1;
                dfs(i, graph, vis);
            }
        }
        
        return ans;
    }
};