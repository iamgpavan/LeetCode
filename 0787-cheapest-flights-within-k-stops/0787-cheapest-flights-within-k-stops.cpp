class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<pair<int, int>> graph[n];
        vector<int> dis(n,1e9);
        queue<pair<int, pair<int,int>>> q;
        
        for(int i=0; i<flights.size(); i++){
            graph[flights[i][0]].push_back({flights[i][1],flights[i][2]});
        }
        q.push({0,{src,0}});
        dis[src] = 0;
        
        while(!q.empty()){
            int node = q.front().second.first;
            int stops = q.front().first;
            int cost = q.front().second.second;
            q.pop();
            if(stops > k)   continue;
            
            for(auto it: graph[node]){
                int adjNode = it.first;
                int adjCost = it.second;
                
                if(cost+adjCost < dis[adjNode] && stops <= k){
                    dis[adjNode] = cost+adjCost;
                    q.push({stops+1, {adjNode, adjCost+cost}});
                }
            }
        }
        
        if(dis[dst] == 1e9) return -1;
        
        return dis[dst];
    }
};