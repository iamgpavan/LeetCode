//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

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
    
    
    int numProvinces(vector<vector<int>> isConnected, int V) {
        // code here
        vector<int> graph[isConnected.size()];
        vector<int> vis(isConnected.size(), 0);
        
        for(int i=0; i<isConnected.size(); i++){
            for(int j=0; j<isConnected[0].size(); j++){
                if(isConnected[i][j] == 1 && i!=j){
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

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int V,x;
        cin>>V;
        
        vector<vector<int>> adj;
        
        for(int i=0; i<V; i++)
        {
            vector<int> temp;
            for(int j=0; j<V; j++)
            {
                cin>>x;
                temp.push_back(x);
            }
            adj.push_back(temp);
        }
        

        Solution ob;
        cout << ob.numProvinces(adj,V) << endl;
    }
    return 0;
}
// } Driver Code Ends