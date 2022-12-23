//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    // Function to return the adjacency list for each vertex.
    vector<vector<int>> printGraph(int V, vector<int> adj[]) {
        // Code here
        // index    0        1       2      3       4     ---> node 14x4 = 52 Bytes == 2xE
        // adj = [[1,4], [0,2,3,4],[1,3],[1,2,4],[0,1,3]] ---> connection
        
        // adj matrix ---> 25x4 = 100 bytes
        //      0   1   2   3   4
        //  0   0   1   0   0   1
        
        //  1   1   0   1   1   1
        
        //  2   0   1   0   1   0
        
        //  3   0   1   1   0   1
        
        //  4   1   1   0   1   0
        
        vector<vector<int>> graph;
        
        for(int i=0; i<V; i++){
            vector<int> vertex;
            vertex.push_back(i);
            for(int j=0; j<adj[i].size(); j++){
                vertex.push_back(adj[i][j]);
            }
            graph.push_back(vertex);
        }
        
        return graph;
    }
};

//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int V, E;
        cin >> V >> E;
        vector<int> adj[V];
        for (int i = 0; i < E; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        Solution obj;
        vector<vector<int>> ans = obj.printGraph(V, adj);
        for (int i = 0; i < ans.size(); i++) {
            for (int j = 0; j < ans[i].size() - 1; j++) {
                cout << ans[i][j] << "-> ";
            }
            cout << ans[i][ans[i].size() - 1];
            cout << endl;
        }
    }
    return 0;
}
// } Driver Code Ends